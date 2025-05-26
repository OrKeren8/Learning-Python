from fastapi import APIRouter

calc_router = APIRouter(prefix="/calculator")

@calc_router.get("/")
async def root():
    return {"message": "Hello World"}

@calc_router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
