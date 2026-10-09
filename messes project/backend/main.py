from fastapi import FastAPI  # type: ignore[reportMissingImports]
from typing import Any

try:
    from fastapi.middleware.cors import CORSMiddleware as _CORSMiddleware  # pyright: ignore[reportAssignmentType, reportMissingImports]
    CORSMiddleware: Any = _CORSMiddleware
except ImportError:  # pragma: no cover
    class _CORSMiddleware:  # type: ignore[no-redef]
        def __init__(self, *args, **kwargs): # type: ignore
            pass

    CORSMiddleware: Any = _CORSMiddleware

import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database create
def create_database():
    connection = sqlite3.connect("messages.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


create_database()


@app.get("/")
def home():
    return {"message": "Messaging App is Running!"}


# Get all messages
@app.get("/messages")
def get_messages(): # type: ignore

    connection = sqlite3.connect("messages.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, username, message FROM messages"
    )

    data = cursor.fetchall()

    connection.close()

    messages = []

    for row in data:
        messages.append({ # type: ignore
            "id": row[0],
            "username": row[1],
            "message": row[2]
        })

    return {"messages": messages} # type: ignore


# Send message
@app.post("/messages")
def send_message(username: str, message: str): # type: ignore

    connection = sqlite3.connect("messages.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO messages (username, message) VALUES (?, ?)",
        (username, message)
    )

    connection.commit()

    message_id = cursor.lastrowid

    connection.close()

    return {
        "id": message_id,
        "username": username,
        "message": message
    } # type: ignore