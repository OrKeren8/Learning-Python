from typing import Optional
from fastapi import APIRouter, Request

from calculator import Calculator
from models import CalculateRequest, Response, HistoryResponse
from exceptions import CalculatorException
from deps import Deps


calc_router = APIRouter(prefix="/calculator")
calculator = Calculator()

@calc_router.get("/health")
async def root():
    return "OK"

@calc_router.post("/independent/calculate", response_model=Response)
async def independent_calculation(req: CalculateRequest) -> Response:
    try:
        res = calculator.calculate(req)
        return Response(result=res, errorMessage=None)
    except CalculatorException as e:
        return Response(result=None, errorMessage=e.message)
    
@calc_router.get("/stack/size")
async def get_stack_size(req: Request):
    res = Response(result=calculator.stack_size, errorMessage=None)
    Deps.get_stack_logger(req.state.request_id).debug(f"Stack size is {calculator.stack_size}")
    return res

@calc_router.put("/stack/arguments")
async def put_stack_arguments(req: CalculateRequest) -> Response:
    for arg in req.arguments:
        calculator._stack.append(arg)
    return Response(result=len(calculator._stack), errorMessage=None)

@calc_router.get("/stack/operate")
async def operate_stack(operation: str) -> Response:
    try:
        res = calculator.calculate_from_stack(operation)
        return Response(result=res, errorMessage=None)
    except CalculatorException as e:
        return Response(result=None, errorMessage=e.message)
    
@calc_router.delete("/stack/arguments")
async def delete_stack_arguments(count: int) -> Response:
    try:
        curr_size = calculator.pop_stack_args(count)
        return Response(result=curr_size, errorMessage=None)
    except CalculatorException as e:
        return Response(result=None, errorMessage=e.message)

@calc_router.get("/history")
async def get_history(flavor: Optional[str] = None) -> HistoryResponse:
    try:
        res = calculator.get_operations_history(flavor)
        return HistoryResponse(result=res, errorMessage=None)
    except CalculatorException as e:
        return HistoryResponse(result=None, errorMessage=e.message)
