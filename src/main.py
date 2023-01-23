from typing import Union, List

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

class wsServiceIn(BaseModel):
    wsCode: str
    param: dict = {}


class wsServiceOut(BaseModel):
    status: str
    message: str
    data: dict = {}


@app.get("/")
async def get_default():
    return {"message": "Hello all bro!!", "framework": "fast-api"}

@app.get("/author")
async def get_author():
    return {"author": "I\'m Samreach!!", "message": "Heheh hello ma bro"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.post("/demo-v2")
async def check_item_service(wsService: wsServiceIn):
    lstParams = wsService.param
    
    for key, value in lstParams.items():
        print(key, value, end='\n')

    return wsServiceOut(status="0", message=wsService.wsCode + " - checked", data=lstParams)
