import json
import os

DB_FILE = "db.json"

DEFAULT_DB = {
    "users": [],
    "products": [],
    "orders": []
}


def load_db():
    if not os.path.exists(DB_FILE):
        save_db(DEFAULT_DB)
        return DEFAULT_DB.copy()

    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        save_db(DEFAULT_DB)
        return DEFAULT_DB.copy()

    return data


def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
