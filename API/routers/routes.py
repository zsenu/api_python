from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from fastapi import APIRouter
from data.filehandler import add_user, add_basket, add_item_to_basket, load_json, save_json
from data.filereader import get_user_by_id, get_basket_by_user_id, get_all_users, get_total_price_of_basket

routers = APIRouter()

@routers.post('/adduser', response_model = User)
def adduser(user: User) -> User:
    try:
        add_user(user.dict())
        return JSONResponse(content = user.dict(), status_code = 201)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))

@routers.post('/addshoppingbag')
def addshoppingbag(userid: int) -> str:
    try:
        basket = {"id": len(load_json()["Baskets"]) + 1, "user_id": userid, "items": []}
        add_basket(basket)
        return JSONResponse(content={"message": "Shopping bag added successfully."}, status_code = 201)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))

@routers.post('/additem', response_model = Basket)
def additem(userid: int, item: Item) -> Basket:
    try:
        add_item_to_basket(userid, item.dict())
        basket_items = get_basket_by_user_id(userid)
        return JSONResponse(content = {"id": userid, "user_id": userid, "items": basket_items}, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))

@routers.put('/updateitem')
def updateitem(userid: int, itemid: int, updateItem: Item) -> Basket:
    try:
        data = load_json()
        basket = next((b for b in data["Baskets"] if b["user_id"] == userid), None)
        if not basket:
            raise HTTPException(status_code = 404, detail = "Basket not found.")
        item = next((i for i in basket["items"] if i["item_id"] == itemid), None)
        if not item:
            raise HTTPException(status_code = 404, detail = "Item not found.")
        item.update(updateItem.dict())
        save_json(data)
        return JSONResponse(content = basket, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))

@routers.delete('/deleteitem')
def deleteitem(userid: int, itemid: int) -> Basket:
    try:
        data = load_json()
        basket = next((b for b in data["Baskets"] if b["user_id"] == userid), None)
        if not basket:
            raise HTTPException(status_code = 404, detail = "Basket not found.")
        basket["items"] = [i for i in basket["items"] if i["item_id"] != itemid]
        save_json(data)
        return JSONResponse(content = basket, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))

@routers.get('/user', response_model = User)
def user(userid: int) -> User:
    try:
        user_data = get_user_by_id(userid)
        return JSONResponse(content = user_data, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code = 404, detail = str(e))

@routers.get('/users', response_model = list[User])
def users() -> list[User]:
    try:
        all_users = get_all_users()
        return JSONResponse(content = all_users, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))

@routers.get('/shoppingbag', response_model = list[Item])
def shoppingbag(userid: int) -> list[Item]:
    try:
        basket_items = get_basket_by_user_id(userid)
        return JSONResponse(content = basket_items, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code = 404, detail = str(e))

@routers.get('/getusertotal')
def getusertotal(userid: int) -> float:
    try:
        total_price = get_total_price_of_basket(userid)
        return JSONResponse(content = {"total_price": total_price}, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code = 404, detail = str(e))