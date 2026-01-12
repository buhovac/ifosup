import asyncio
import json
import threading
import queue
import tkinter as tk
from tkinter import ttk, messagebox

import websockets

# -----------------------------
# Queues (thread-safe)
# -----------------------------
incoming = queue.Queue()   # messages from network -> GUI
outgoing = queue.Queue()   # messages from GUI -> network


class ChatGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Chat (Tkinter + WebSocket)")

        # --- Connection frame ---
        conn = ttk.Frame(root, padding=10)
        conn.pack(fill="x")

        ttk.Label(conn, text="Host").grid(row=0, column=0, sticky="w")
        self.host_var = tk.StringVar(value="localhost")
        ttk.Entry(conn, textvariable=self.host_var, width=18).grid(row=0, column=1, padx=5)

        ttk.Label(conn, text="Port").grid(row=0, column=2, sticky="w")
        self.port_var = tk.StringVar(value="6789")
        ttk.Entry(conn, textvariable=self.port_var, width=8).grid(row=0, column=3, padx=5)

        ttk.Label(conn, text="Username").grid(row=0, column=4, sticky="w")
        self.user_var = tk.StringVar(value="user")
        ttk.Entry(conn, textvariable=self.user_var, width=14).grid(row=0, column=5, padx=5)

        self.connect_btn = ttk.Button(conn, text="Connect", command=self.on_connect)
        self.connect_btn.grid(row=0, column=6, padx=8)

        self.status_var = tk.StringVar(value="Not connected")
        ttk.Label(conn, textvariable=self.status_var).grid(row=1, column=0, columnspan=7, sticky="w", pady=(6, 0))

        # --- Rooms frame ---
        rooms_frame = ttk.Frame(root, padding=(10, 0, 10, 10))
        rooms_frame.pack(fill="x")

        ttk.Label(rooms_frame, text="Rooms:").grid(row=0, column=0, sticky="w")

        self.rooms_var = tk.StringVar(value=["general"])
        self.rooms_list = tk.Listbox(rooms_frame, listvariable=self.rooms_var, height=4)
        self.rooms_list.grid(row=0, column=1, sticky="we", padx=5)
        rooms_frame.columnconfigure(1, weight=1)

        self.refresh_btn = ttk.Button(rooms_frame, text="Refresh", command=self.on_refresh_rooms, state="disabled")
        self.refresh_btn.grid(row=0, column=2, padx=5)

        self.join_btn = ttk.Button(rooms_frame, text="Join", command=self.on_join_room, state="disabled")
        self.join_btn.grid(row=0, column=3, padx=5)

        self.current_room_var = tk.StringVar(value="general")
        ttk.Label(rooms_frame, text="Current:").grid(row=1, column=0, sticky="w", pady=(6, 0))
        ttk.Label(rooms_frame, textvariable=self.current_room_var).grid(row=1, column=1, sticky="w", pady=(6, 0))

        # --- Chat display ---
        chat_frame = ttk.Frame(root, padding=10)
        chat_frame.pack(fill="both", expand=True)

        self.chat = tk.Text(chat_frame, height=16, state="disabled", wrap="word")
        self.chat.pack(fill="both", expand=True)

        # --- Message entry ---
        bottom = ttk.Frame(root, padding=10)
        bottom.pack(fill="x")

        self.msg_var = tk.StringVar()
        self.msg_entry = ttk.Entry(bottom, textvariable=self.msg_var)
        self.msg_entry.pack(side="left", fill="x", expand=True)

        self.send_btn = ttk.Button(bottom, text="Send", command=self.on_send, state="disabled")
        self.send_btn.pack(side="left", padx=8)

        # Poll incoming messages
        self.root.after(100, self.process_incoming)

        self.net_thread = None

    # -----------------------------
    # GUI actions
    # -----------------------------
    def on_connect(self):
        host = self.host_var.get().strip() or "localhost"
        port = self.port_var.get().strip() or "6789"
        username = self.user_var.get().strip() or "user"

        if self.net_thread and self.net_thread.is_alive():
            messagebox.showinfo("Info", "Already connected (or connecting).")
            return

        self.status_var.set(f"Connecting to ws://{host}:{port} ...")
        self.connect_btn.config(state="disabled")

        self.net_thread = threading.Thread(
            target=run_network_loop,
            args=(host, port, username),
            daemon=True
        )
        self.net_thread.start()

    def on_refresh_rooms(self):
        outgoing.put({"action": "list_rooms"})

    def on_join_room(self):
        sel = self.rooms_list.curselection()
        if not sel:
            return
        room = self.rooms_list.get(sel[0])
        outgoing.put({"action": "join_room", "room": room})

    def on_send(self):
        text = self.msg_var.get().strip()
        if not text:
            return
        outgoing.put({"action": "send_message", "text": text})
        self.msg_var.set("")

    # -----------------------------
    # Consume incoming queue
    # -----------------------------
    def process_incoming(self):
        try:
            while True:
                msg = incoming.get_nowait()
                self.handle_server_msg(msg)
        except queue.Empty:
            pass
        self.root.after(100, self.process_incoming)

    def handle_server_msg(self, data: dict):
        if data.get("_internal") == "connected":
            self.status_var.set("Connected ✅")
            self.refresh_btn.config(state="normal")
            self.join_btn.config(state="normal")
            self.send_btn.config(state="normal")
            self.msg_entry.focus_set()
            return

        if data.get("_internal") == "disconnected":
            self.status_var.set("Disconnected ❌")
            self.connect_btn.config(state="normal")
            self.refresh_btn.config(state="disabled")
            self.join_btn.config(state="disabled")
            self.send_btn.config(state="disabled")
            return

        if data.get("type") == "rooms_list":
            self.rooms_var.set(data.get("rooms", []))
            return

        if data.get("type") == "system":
            if data.get("event") == "room_changed":
                self.current_room_var.set(data.get("room", ""))
            self.append_chat(f"[system] {data}")
            return

        if data.get("type") == "message":
            room = data.get("room", "?")
            who = data.get("from", "?")
            text = data.get("text", "")
            self.append_chat(f"[{room}] {who}: {text}")
            return

        if data.get("type") == "error":
            self.append_chat(f"[error] {data.get('message')}")
            return

        self.append_chat(str(data))

    def append_chat(self, line: str):
        self.chat.config(state="normal")
        self.chat.insert("end", line + "\n")
        self.chat.see("end")
        self.chat.config(state="disabled")


# -----------------------------
# Network (asyncio in thread)
# -----------------------------
async def websocket_worker(host: str, port: str, username: str):
    url = f"ws://{host}:{port}"
    try:
        async with websockets.connect(url) as ws:
            # Register
            await ws.send(json.dumps({"action": "register", "username": username}))
            incoming.put({"_internal": "connected"})

            recv_task = asyncio.create_task(recv_from_server(ws))
            send_task = asyncio.create_task(send_to_server(ws))

            done, pending = await asyncio.wait(
                {recv_task, send_task},
                return_when=asyncio.FIRST_COMPLETED
            )
            for t in pending:
                t.cancel()

    except Exception as e:
        incoming.put({"type": "error", "message": f"Connection error: {e}"})
    finally:
        incoming.put({"_internal": "disconnected"})


async def recv_from_server(ws):
    async for msg in ws:
        try:
            incoming.put(json.loads(msg))
        except json.JSONDecodeError:
            incoming.put({"type": "error", "message": f"Invalid JSON from server: {msg}"})


async def send_to_server(ws):
    while True:
        data = await asyncio.to_thread(outgoing.get)
        await ws.send(json.dumps(data))


def run_network_loop(host: str, port: str, username: str):
    asyncio.run(websocket_worker(host, port, username))


# -----------------------------
# Run GUI
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    try:
        ttk.Style().theme_use("clam")
    except Exception:
        pass
    ChatGUI(root)
    root.mainloop()
