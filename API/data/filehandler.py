import json
from typing import Dict, Any

JSON_FILE_PATH = "./data/data.json"

def load_json() -> Dict[str, Any]:
    try:
        with open(JSON_FILE_PATH, "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise ValueError(f"json file could not be found at {JSON_FILE_PATH}")

def save_json(data: Dict[str, Any]) -> None:
    with open(JSON_FILE_PATH, "w", encoding = "utf-8") as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)

def add_user(user: Dict[str, Any]) -> None:
    data = load_json()
    if any(existing_user["id"] == user["id"] for existing_user in data["Users"]):
        raise ValueError(f"user with id {user['id']} already exists")
    data["Users"].append(user)
    save_json(data)

def add_basket(basket: Dict[str, Any]) -> None:
    data = load_json()
    if not any(user["id"] == basket["user_id"] for user in data["Users"]):
        raise ValueError(f"user with id {basket['user_id']} does not exist")
    if any(existing_basket["id"] == basket["id"] for existing_basket in data["Baskets"]):
        raise ValueError(f"basket with id {basket['id']} already exists")
    data["Baskets"].append(basket)
    save_json(data)

def add_item_to_basket(user_id: int, item: Dict[str, Any]) -> None:
    data = load_json()
    basket = next((b for b in data["Baskets"] if b["user_id"] == user_id), None)
    if not basket:
        raise ValueError(f"could not find basket for user with id {user_id}")
    basket["items"].append(item)
    save_json(data)