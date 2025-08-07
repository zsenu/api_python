from fastapi import FastAPI
from schemas.schema import ShopName
from routers.routes import routers as routes_router

# python -m uvicorn main:app --reload --port 9000

app = FastAPI()

app.include_router(routes_router, tags=["Bolt"])

@app.get('/', tags=["Root"])
def route():
    return {'Welcome to ': ShopName}