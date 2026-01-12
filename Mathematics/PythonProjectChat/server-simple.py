import asyncio
import json
import logging
import websockets
from websockets.exceptions import ConnectionClosed

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("chat_server")

clients = {}              # ws -> {"username": str, "room": str|None}
rooms = {"general": set()}  # room -> set(ws)


# ---------- small helpers ----------

def rooms_list():
    return list(rooms.keys())

def client(ws):
    return clients.get(ws)

async def send(ws, data: dict):
    try:
        await ws.send(json.dumps(data))
    except ConnectionClosed:
        pass

async def error(ws, msg: str):
    await send(ws, {"type": "error", "message": msg})

async def broadcast(room: str, data: dict, exclude=None):
    if room not in rooms:
        return
    msg = json.dumps(data)
    targets = [c for c in rooms[room] if c is not exclude]
    if targets:
        await asyncio.gather(*[c.send(msg) for c in targets], return_exceptions=True)

def require_registered(ws):
    info = client(ws)
    return info


# ---------- actions ----------

async def action_register(ws, data):
    username = (data.get("username") or "").strip()
    if not username:
        return await error(ws, "Missing 'username'")

    if any(info["username"] == username for info in clients.values()):
        return await error(ws, "Username taken")

    clients[ws] = {"username": username, "room": "general"}
    rooms["general"].add(ws)

    log.info("Registered '%s' in 'general'", username)

    await send(ws, {"type": "system", "event": "registered", "username": username, "room": "general"})
    await send(ws, {"type": "rooms_list", "rooms": rooms_list()})
    await broadcast("general", {"type": "system", "event": "user_joined", "room": "general", "username": username}, exclude=ws)


async def action_list_rooms(ws, data):
    await send(ws, {"type": "rooms_list", "rooms": rooms_list()})


async def action_create_room(ws, data):
    info = require_registered(ws)
    if not info:
        return await error(ws, "Register first")

    room = (data.get("room") or "").strip()
    if not room:
        return await error(ws, "Missing 'room'")
    if room in rooms:
        return await error(ws, "Room exists")

    rooms[room] = set()
    log.info("Room '%s' created by '%s'", room, info["username"])

    await send(ws, {"type": "rooms_list", "rooms": rooms_list()})


async def action_join_room(ws, data):
    info = require_registered(ws)
    if not info:
        return await error(ws, "Register first")

    new_room = (data.get("room") or "").strip()
    if not new_room:
        return await error(ws, "Missing 'room'")
    if new_room not in rooms:
        return await error(ws, "Room not found")

    old_room = info["room"]
    username = info["username"]

    # leave old room (if any)
    if old_room and ws in rooms.get(old_room, set()):
        rooms[old_room].remove(ws)
        await broadcast(old_room, {"type": "system", "event": "user_left", "room": old_room, "username": username}, exclude=ws)

    # join new room
    rooms[new_room].add(ws)
    info["room"] = new_room

    log.info("'%s' moved %s -> %s", username, old_room, new_room)

    await send(ws, {"type": "system", "event": "room_changed", "room": new_room})
    await broadcast(new_room, {"type": "system", "event": "user_joined", "room": new_room, "username": username}, exclude=ws)


async def action_leave_room(ws, data):
    info = require_registered(ws)
    if not info:
        return await error(ws, "Register first")

    room = info["room"]
    if not room:
        return  # already not in a room

    username = info["username"]

    if ws in rooms.get(room, set()):
        rooms[room].remove(ws)

    info["room"] = None
    log.info("'%s' left '%s'", username, room)

    await send(ws, {"type": "system", "event": "left_room", "room": room})
    await broadcast(room, {"type": "system", "event": "user_left", "room": room, "username": username}, exclude=ws)


async def action_send_message(ws, data):
    info = require_registered(ws)
    if not info:
        return await error(ws, "Register first")

    text = (data.get("text") or "").strip()
    if not text:
        return await error(ws, "Empty message")

    room = info["room"]
    if not room:
        return await error(ws, "Not in a room")

    payload = {"type": "message", "room": room, "from": info["username"], "text": text}
    log.info("Message from '%s' in '%s': %s", info["username"], room, text)

    await broadcast(room, payload)


ACTIONS = {
    "register": action_register,
    "list_rooms": action_list_rooms,
    "create_room": action_create_room,
    "join_room": action_join_room,
    "leave_room": action_leave_room,
    "send_message": action_send_message,
}


# ---------- main connection handler ----------

async def handle(ws):
    log.info("New connection from %s", ws.remote_address)
    try:
        async for msg in ws:
            try:
                data = json.loads(msg)
            except json.JSONDecodeError:
                await error(ws, "Invalid JSON")
                continue

            action = data.get("action")
            if not action:
                await error(ws, "Missing 'action'")
                continue

            func = ACTIONS.get(action)
            if not func:
                await error(ws, f"Unknown action '{action}'")
                continue

            await func(ws, data)

    finally:
        info = clients.pop(ws, None)
        if info:
            username = info["username"]
            room = info["room"]
            if room and ws in rooms.get(room, set()):
                rooms[room].remove(ws)
                await broadcast(room, {"type": "system", "event": "user_left", "room": room, "username": username})
            log.info("Disconnected '%s'", username)
        else:
            log.info("Disconnected unregistered client")


async def main():
    async with websockets.serve(handle, "localhost", 6789):
        log.info("Server running at ws://localhost:6789")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
