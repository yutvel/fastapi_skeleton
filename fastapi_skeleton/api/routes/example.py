from typing import Optional

from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_skeleton.core import security
from fastapi_skeleton.models.item import Item

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(
    item_id: int,
    q: Optional[str] = None,
    authenticated: bool = Depends(security.validate_request),
):
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    authenticated: bool = Depends(security.validate_request),
):
    return {"item_name": item.name, "price": item.price, "item_id": item_id}
