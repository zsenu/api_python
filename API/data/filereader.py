import json
from typing import Dict, Any, List

JSON_FILE_PATH = "./data/data.json"

def load_json() -> Dict[str, Any]:
    try:
        with open(JSON_FILE_PATH, "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise ValueError(f"json file could not be found at {JSON_FILE_PATH}")

def get_user_by_id(user_id: int) -> Dict[str, Any]:
    data = load_json()
    user = next((user for user in data["Users"] if user["id"] == user_id), None)
    if not user:
        raise ValueError(f"could not find user with id {user_id}")
    return user

def get_basket_by_user_id(user_id: int) -> List[Dict[str, Any]]:
    data = load_json()
    basket = next((basket for basket in data["Baskets"] if basket["user_id"] == user_id), None)
    if not basket:
        raise ValueError(f"could not find basket for user with id {user_id}")
    return basket["items"]

def get_all_users() -> List[Dict[str, Any]]:
    data = load_json()
    return data["Users"]

def get_total_price_of_basket(user_id: int) -> float:
    items = get_basket_by_user_id(user_id)
    total_price = sum(item["price"] * item["quantity"] for item in items)
    return total_price