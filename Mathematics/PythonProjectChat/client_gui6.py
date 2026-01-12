import sys
import json
import asyncio
import threading

import websockets
from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QListWidget,
    QGroupBox, QMessageBox
)

# -----------------------------
# Signal bridge (thread -> GUI)
# -----------------------------
class Bridge(QObject):
    received = Signal(dict)
    status = Signal(str)

bridge = Bridge()

net_loop = None
ws_client = None


# -----------------------------
# Network (asyncio in thread)
# -----------------------------
async def ws_connect(host: str, port: str, username: str):
    global ws_client
    url = f"ws://{host}:{port}"
    bridge.status.emit(f"Connecting to {url} ...")

    ws_client = await websockets.connect(url)

    # Register
    await ws_client.send(json.dumps({"action": "register", "username": username}))
    bridge.status.emit(f"Connected ✅ as '{username}'")

    # Start receiver loop
    asyncio.create_task(ws_recv_loop())

    # Ask rooms immediately
    await ws_client.send(json.dumps({"action": "list_rooms"}))


async def ws_recv_loop():
    global ws_client
    try:
        async for msg in ws_client:
            try:
                bridge.received.emit(json.loads(msg))
            except json.JSONDecodeError:
                bridge.received.emit({"type": "error", "message": f"Invalid JSON: {msg}"})
    except Exception as e:
        bridge.status.emit(f"Disconnected ❌ ({e})")


async def ws_send(data: dict):
    global ws_client
    if ws_client is None:
        bridge.received.emit({"type": "error", "message": "Not connected."})
        return
    await ws_client.send(json.dumps(data))


def start_network_thread():
    global net_loop
    net_loop = asyncio.new_event_loop()

    def runner():
        asyncio.set_event_loop(net_loop)
        net_loop.run_forever()

    t = threading.Thread(target=runner, daemon=True)
    t.start()


def run_coro(coro):
    if net_loop is None:
        bridge.received.emit({"type": "error", "message": "Network loop not started."})
        return
    asyncio.run_coroutine_threadsafe(coro, net_loop)


# -----------------------------
# GUI
# -----------------------------
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat - PySide6 + WebSocket")

        # ---------- Connection row ----------
        self.host = QLineEdit("localhost")
        self.port = QLineEdit("6789")
        self.username = QLineEdit("user")
        self.connect_btn = QPushButton("Connect")

        top = QHBoxLayout()
        top.addWidget(QLabel("Host"))
        top.addWidget(self.host)
        top.addWidget(QLabel("Port"))
        top.addWidget(self.port)
        top.addWidget(QLabel("Username"))
        top.addWidget(self.username)
        top.addWidget(self.connect_btn)

        # ---------- Status ----------
        self.status_lbl = QLabel("Not connected")
        self.current_room_lbl = QLabel("Current room: -")

        # ---------- Rooms panel ----------
        rooms_box = QGroupBox("Rooms")
        rooms_layout = QVBoxLayout()

        self.rooms_list = QListWidget()

        btn_row1 = QHBoxLayout()
        self.refresh_rooms_btn = QPushButton("Refresh")
        self.join_room_btn = QPushButton("Join")
        btn_row1.addWidget(self.refresh_rooms_btn)
        btn_row1.addWidget(self.join_room_btn)

        create_row = QHBoxLayout()
        self.create_room_input = QLineEdit()
        self.create_room_input.setPlaceholderText("new room name")
        self.create_room_btn = QPushButton("Create")
        create_row.addWidget(self.create_room_input)
        create_row.addWidget(self.create_room_btn)

        self.leave_room_btn = QPushButton("Leave current room")

        # disabled until connected
        for b in (self.refresh_rooms_btn, self.join_room_btn, self.create_room_btn, self.leave_room_btn):
            b.setEnabled(False)

        rooms_layout.addWidget(self.rooms_list)
        rooms_layout.addLayout(btn_row1)
        rooms_layout.addLayout(create_row)
        rooms_layout.addWidget(self.leave_room_btn)
        rooms_box.setLayout(rooms_layout)

        # ---------- Chat panel ----------
        chat_box = QGroupBox("Chat")
        chat_layout = QVBoxLayout()

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        msg_row = QHBoxLayout()
        self.msg = QLineEdit()
        self.send_btn = QPushButton("Send")
        self.send_btn.setEnabled(False)
        msg_row.addWidget(self.msg)
        msg_row.addWidget(self.send_btn)

        chat_layout.addWidget(self.chat)
        chat_layout.addLayout(msg_row)
        chat_box.setLayout(chat_layout)

        # ---------- Middle layout ----------
        middle = QHBoxLayout()
        middle.addWidget(rooms_box, 1)
        middle.addWidget(chat_box, 3)

        # ---------- Root layout ----------
        layout = QVBoxLayout()
        layout.addLayout(top)
        layout.addWidget(self.status_lbl)
        layout.addWidget(self.current_room_lbl)
        layout.addLayout(middle)
        self.setLayout(layout)

        # ---------- Events ----------
        self.connect_btn.clicked.connect(self.on_connect)
        self.send_btn.clicked.connect(self.on_send)
        self.msg.returnPressed.connect(self.on_send)

        self.refresh_rooms_btn.clicked.connect(self.on_refresh_rooms)
        self.join_room_btn.clicked.connect(self.on_join_selected_room)
        self.rooms_list.itemDoubleClicked.connect(lambda _: self.on_join_selected_room())

        self.create_room_btn.clicked.connect(self.on_create_room)
        self.create_room_input.returnPressed.connect(self.on_create_room)

        self.leave_room_btn.clicked.connect(self.on_leave_room)

        bridge.received.connect(self.on_received)
        bridge.status.connect(self.on_status)

        self.current_room = None

    # -----------------------------
    # Actions
    # -----------------------------
    def on_connect(self):
        h = self.host.text().strip() or "localhost"
        p = self.port.text().strip() or "6789"
        u = self.username.text().strip() or "user"

        self.connect_btn.setEnabled(False)
        run_coro(ws_connect(h, p, u))

    def on_refresh_rooms(self):
        run_coro(ws_send({"action": "list_rooms"}))

    def on_join_selected_room(self):
        item = self.rooms_list.currentItem()
        if not item:
            QMessageBox.information(self, "Info", "Select a room first.")
            return
        room = item.text().strip()
        run_coro(ws_send({"action": "join_room", "room": room}))

    def on_create_room(self):
        room = self.create_room_input.text().strip()
        if not room:
            QMessageBox.information(self, "Info", "Enter a room name.")
            return
        self.create_room_input.clear()
        run_coro(ws_send({"action": "create_room", "room": room}))

    def on_leave_room(self):
        run_coro(ws_send({"action": "leave_room"}))

    def on_send(self):
        text = self.msg.text().strip()
        if not text:
            return
        self.msg.clear()
        run_coro(ws_send({"action": "send_message", "text": text}))

    # -----------------------------
    # Bridge handlers
    # -----------------------------
    def on_status(self, text: str):
        self.status_lbl.setText(text)

        if text.startswith("Connected"):
            self.send_btn.setEnabled(True)
            self.refresh_rooms_btn.setEnabled(True)
            self.join_room_btn.setEnabled(True)
            self.create_room_btn.setEnabled(True)
            self.leave_room_btn.setEnabled(True)
            return

        if text.startswith("Disconnected"):
            self.send_btn.setEnabled(False)
            self.refresh_rooms_btn.setEnabled(False)
            self.join_room_btn.setEnabled(False)
            self.create_room_btn.setEnabled(False)
            self.leave_room_btn.setEnabled(False)
            self.connect_btn.setEnabled(True)
            self.current_room = None
            self.current_room_lbl.setText("Current room: -")
            return

    def on_received(self, data: dict):
        t = data.get("type")

        if t == "rooms_list":
            rooms = data.get("rooms", [])
            self.rooms_list.clear()
            for r in rooms:
                self.rooms_list.addItem(str(r))
            self.chat.append(f"[rooms] {rooms}")
            return

        if t == "system":
            event = data.get("event")

            if event == "registered":
                self.current_room = data.get("room")
                self.current_room_lbl.setText(f"Current room: {self.current_room}")
                self.chat.append(f"[system] registered in '{self.current_room}'")
                return

            if event == "room_changed":
                self.current_room = data.get("room")
                self.current_room_lbl.setText(f"Current room: {self.current_room}")
                self.chat.append(f"[system] room changed -> '{self.current_room}'")
                return

            if event == "left_room":
                left = data.get("room")
                self.current_room = None
                self.current_room_lbl.setText("Current room: -")
                self.chat.append(f"[system] left room '{left}'")
                return

            if event == "user_joined":
                self.chat.append(f"[system] user_joined: {data.get('username')} in {data.get('room')}")
                return

            if event == "user_left":
                self.chat.append(f"[system] user_left: {data.get('username')} from {data.get('room')}")
                return

            self.chat.append(f"[system] {data}")
            return

        if t == "message":
            room = data.get("room", "?")
            who = data.get("from", "?")
            text = data.get("text", "")
            self.chat.append(f"[{room}] {who}: {text}")
            return

        if t == "error":
            self.chat.append(f"[error] {data.get('message')}")
            return

        self.chat.append(str(data))


def main():
    start_network_thread()
    app = QApplication(sys.argv)
    w = ChatWindow()
    w.resize(1050, 560)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
