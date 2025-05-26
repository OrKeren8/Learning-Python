from fastapi import APIRouter


calc_router = APIRouter(prefix="/calculator")


@calc_router.get("/health")
async def root():
    return "OK"

@calc_router.post("/independent/calculate")
async def independent_calculation(data: dict):
    