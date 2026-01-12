import asyncio
import json
import websockets


async def send_loop(ws, username):
    """Čita komande iz inputa i šalje JSON poruke serveru."""
    print(
        f"Nom d'utilisateur: {username}\nCommandes: /rooms, /create <room>, /join <room>, /leave, /msg <text>, /raw <JSON>, /quit")

    while True:
        try:
            raw_line = await asyncio.to_thread(input, "> ")
            line = raw_line.strip()
            if not line:
                continue

            # Razdvajamo prvu riječ (komandu) od ostatka
            if ' ' in line:
                cmd, rest = line.split(maxsplit=1)
            else:
                cmd = line
                rest = ""

            # Dictionary sa handlerima – SVAKI handler prima "rest" direktno
            if cmd == "/rooms":
                data = {"action": "list_rooms"}
            elif cmd == "/create":
                if not rest:
                    print("Utilisation : /create <nom_du_salon>")
                    continue
                data = {"action": "create_room", "room": rest.strip()}
            elif cmd == "/join":
                if not rest:
                    print("Utilisation : /join <nom_du_salon>")
                    continue
                data = {"action": "join_room", "room": rest.strip()}
            elif cmd == "/leave":
                data = {"action": "leave_room"}
            elif cmd == "/msg":
                if not rest:
                    print("Utilisation : /msg <message>")
                    continue
                data = {"action": "send_message", "text": rest.strip()}
            elif cmd == "/raw":
                if not rest:
                    print("Utilisation : /raw <JSON>")
                    continue
                try:
                    data = json.loads(rest)
                except json.JSONDecodeError:
                    print("JSON invalide dans /raw.")
                    continue
            elif cmd == "/quit":
                await ws.close()
                return
            else:
                # Ako nije komanda – šalje se kao obična poruka
                data = {"action": "send_message", "text": line}

            await ws.send(json.dumps(data))
        except (EOFError, KeyboardInterrupt):
            await ws.close()
            return


async def recv_loop(ws):
    """Prima i ispisuje poruke od servera."""
    try:
        async for msg in ws:
            try:
                data = json.loads(msg)
                print("\n Reçu:\n" + json.dumps(data, indent=2))
            except json.JSONDecodeError:
                print(f"[Brut] {msg}")
    except websockets.exceptions.ConnectionClosed:
        print("🔌 Connexion fermée.")


async def main():
    host = input("IP serveur (def: localhost): ").strip() or "localhost"
    port = input("Port (def: 6789): ").strip() or "6789"
    username = input("Username: ").strip() or "user"

    url = f"ws://{host}:{port}"
    async with websockets.connect(url) as ws:
        await ws.send(json.dumps({"action": "register", "username": username}))
        print(f"Registré comme '{username}'")

        send_task = asyncio.create_task(send_loop(ws, username))
        recv_task = asyncio.create_task(recv_loop(ws))

        await asyncio.wait([send_task, recv_task], return_when=asyncio.FIRST_COMPLETED)
        for task in [send_task, recv_task]:
            if not task.done(): task.cancel()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nArrêt par utilisateur.")