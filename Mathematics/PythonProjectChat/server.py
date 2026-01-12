import asyncio
import json
import websockets

clients = {}
rooms = {"general": set()}

async def send_json(ws, data):
    try:
        await ws.send(json.dumps(data))
    except websockets.exceptions.ConnectionClosed:
        pass


async def send_error(ws, message):
    await send_json(ws, {"type": "error", "message": message})


async def send_rooms_list(ws):
    await send_json(ws, {"type": "rooms_list", "rooms": list(rooms.keys())})


async def broadcast(room_name, data, exclude=None):
    if room_name not in rooms:
        return

    msg = json.dumps(data)
    for client_ws in list(rooms[room_name]):
        if exclude is not None and client_ws == exclude:
            continue
        try:
            await client_ws.send(msg)
        except websockets.exceptions.ConnectionClosed:
            pass


def get_client(ws):
    return clients.get(ws)

# Actions
async def handle_register(ws, data):
    username = data.get("username")
    if not username:
        await send_error(ws, "Missing 'username'")
        return

    for info in clients.values():
        if info["username"] == username:
            await send_error(ws, "Username taken")
            return

    clients[ws] = {"username": username, "room": "general"}
    rooms["general"].add(ws)

    print(f"[REGISTER] {username} joined 'general'")

    await send_json(ws, {"type": "system", "event": "registered", "username": username, "room": "general"})
    await send_rooms_list(ws)

    await broadcast(
        "general",
        {"type": "system", "event": "user_joined", "room": "general", "username": username},
        exclude=ws
    )

async def handle_list_rooms(ws, data):
    await send_rooms_list(ws)

async def handle_create_room(ws, data):
    info = get_client(ws)
    if info is None:
        await send_error(ws, "Register first")
        return

    room = data.get("room")
    if not room:
        await send_error(ws, "Missing 'room'")
        return

    if room in rooms:
        await send_error(ws, "Room exists")
        return

    rooms[room] = set()
    print(f"[CREATE] room='{room}' by user='{info['username']}'")

    await send_rooms_list(ws)


async def handle_join_room(ws, data):
    info = get_client(ws)
    if info is None:
        await send_error(ws, "Register first")
        return

    new_room = data.get("room")
    if not new_room:
        await send_error(ws, "Missing 'room'")
        return

    if new_room not in rooms:
        await send_error(ws, "Room not found")
        return

    old_room = info["room"]
    username = info["username"]

    if old_room is not None and ws in rooms.get(old_room, set()):
        rooms[old_room].remove(ws)
        await broadcast(
            old_room,
            {"type": "system", "event": "user_left", "room": old_room, "username": username},
            exclude=ws
        )

    rooms[new_room].add(ws)
    info["room"] = new_room

    print(f"[JOIN] {username}: {old_room} -> {new_room}")

    await send_json(ws, {"type": "system", "event": "room_changed", "room": new_room})

    await broadcast(
        new_room,
        {"type": "system", "event": "user_joined", "room": new_room, "username": username},
        exclude=ws
    )


async def handle_leave_room(ws, data):
    info = get_client(ws)
    if info is None:
        await send_error(ws, "Register first")
        return

    room = info["room"]
    if room is None:
        return

    username = info["username"]

    if ws in rooms.get(room, set()):
        rooms[room].remove(ws)

    info["room"] = None

    print(f"[LEAVE] {username} left '{room}'")

    await send_json(ws, {"type": "system", "event": "left_room", "room": room})

    await broadcast(
        room,
        {"type": "system", "event": "user_left", "room": room, "username": username},
        exclude=ws
    )


async def handle_send_message(ws, data):
    info = get_client(ws)
    if info is None:
        await send_error(ws, "Register first")
        return

    text = data.get("text")
    if not text:
        await send_error(ws, "Empty message")
        return

    room = info["room"]
    if room is None:
        await send_error(ws, "Not in a room")
        return

    payload = {"type": "message", "room": room, "from": info["username"], "text": text}
    print(f"[MSG] ({room}) {info['username']}: {text}")

    await broadcast(room, payload)

# Dispatch
async def handle_action(ws, data):
    action = data.get("action")
    if not action:
        await send_error(ws, "Missing 'action'")
        return

    if action == "register":
        await handle_register(ws, data)
    elif action == "list_rooms":
        await handle_list_rooms(ws, data)
    elif action == "create_room":
        await handle_create_room(ws, data)
    elif action == "join_room":
        await handle_join_room(ws, data)
    elif action == "leave_room":
        await handle_leave_room(ws, data)
    elif action == "send_message":
        await handle_send_message(ws, data)
    else:
        await send_error(ws, "Unknown action '%s'" % action)


# Main ws handler
async def handle(ws):
    print(f"[CONNECT] {ws.remote_address}")
    try:
        async for msg in ws:
            try:
                data = json.loads(msg)
            except json.JSONDecodeError:
                await send_error(ws, "Invalid JSON")
                continue

            await handle_action(ws, data)

    finally:
        info = clients.pop(ws, None)
        if info is not None:
            username = info["username"]
            room = info["room"]

            if room is not None and ws in rooms.get(room, set()):
                rooms[room].remove(ws)
                await broadcast(
                    room,
                    {"type": "system", "event": "user_left", "room": room, "username": username},
                    exclude=ws
                )

            print(f"[DISCONNECT] {username}")
        else:
            print("[DISCONNECT] unregistered client")


async def main():
    async with websockets.serve(handle, "localhost", 6789):
        print("Server at ws://localhost:6789")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
