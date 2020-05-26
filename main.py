from fastapi import FastAPI
from request import request_map, save_in_db, list_items_db, list_collections_from_mongo
import pymongo
import json


app = FastAPI()


@app.get("/get-bens")
def get_bens():
    bens = list_items_db()
    return json.loads(bens)


@app.get("/request-get-bens")
def request_and_get_bens():
    request_map()
    bens = list_items_db()
    return json.loads(bens)


@app.get("/request-portal")
def request_portal():
    request_map()
    return {"Request": "Done"}
