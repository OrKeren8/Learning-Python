from fastapi import APIRouter

from calculator import Calculator
from models import CalculateRequest, Response
from exceptions import CalculatorException


calc_router = APIRouter(prefix="/calculator")


@calc_router.get("/health")
async def root():
    return "OK"

@calc_router.post("/independent/calculate", response_model=Response)
async def independent_calculation(req: CalculateRequest) -> Response:
    try:
        res = Calculator.calculate(req)
        return Response(result=res, errorMessage=None)
    except CalculatorException as e:
        return Response(result=None, errorMessage=e.message)