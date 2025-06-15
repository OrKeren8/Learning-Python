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
async def independent_calculation(req: CalculateRequest, req_metadata: Request) -> Response:
    try:
        res = calculator.calculate(req)
        op_name = req.operation.lower() if req.operation else ''
        Deps.get_independent_logger(req_metadata.state.request_id).info(f"Performing operation {op_name}. Result is {res}")
        args = ", ".join(str(x) for x in req.arguments)
        Deps.get_independent_logger(req_metadata.state.request_id).debug(f"Performing operation: {op_name}({args}) = {res}")
        return Response(result=res, errorMessage=None)
    except CalculatorException as e:
        Deps.get_independent_logger(req_metadata.state.request_id).error(f"Server encountered an error ! message: {e.message}")
        return Response(result=None, errorMessage=e.message)
    
@calc_router.get("/stack/size")
async def get_stack_size(req_metadata: Request):
    res = Response(result=calculator.stack_size, errorMessage=None)
    Deps.get_stack_logger(req_metadata.state.request_id).info(f"Stack size is {calculator.stack_size}")
    Deps.get_stack_logger(req_metadata.state.request_id).debug(f"Stack content (first == top): [{calculator.get_stack_content()}]")
    return res

@calc_router.put("/stack/arguments")
async def put_stack_arguments(req: CalculateRequest, req_metadata: Request) -> Response:
    before_size = calculator.stack_size
    total_args = len(req.arguments)
    for arg in req.arguments:
        calculator._stack.append(arg)
    Deps.get_stack_logger(req_metadata.state.request_id).info(f"Adding total of {total_args} argument(s) to the stack | Stack size: {calculator.stack_size}")
    args = ", ".join(str(x) for x in req.arguments)
    Deps.get_stack_logger(req_metadata.state.request_id).debug(f"Adding arguments: {args} | Stack size before {before_size} | stack size after {calculator.stack_size}")
    return Response(result=len(calculator._stack), errorMessage=None)

@calc_router.get("/stack/operate")
async def operate_stack(operation: str, req_metadata: Request) -> Response:
    try:
        res, args_str = calculator.calculate_from_stack(operation)
        Deps.get_stack_logger(req_metadata.state.request_id).info(f"Performing operation {operation.lower()}. Result is {res} | stack size: {calculator.stack_size}")
        Deps.get_stack_logger(req_metadata.state.request_id).debug(f"Performing operation: {operation.lower()}({args_str}) = {res}")
        return Response(result=res, errorMessage=None)
    except CalculatorException as e:
        Deps.get_stack_logger(req_metadata.state.request_id).error(f"Server encountered an error ! message: {e.message}")
        return Response(result=None, errorMessage=e.message)
    
@calc_router.delete("/stack/arguments")
async def delete_stack_arguments(count: int, req_metadata: Request) -> Response:
    try:
        curr_size = calculator.pop_stack_args(count)
        Deps.get_stack_logger(req_metadata.state.request_id).info(f"Removing total {count} argument(s) from the stack | Stack size: {curr_size}")
        return Response(result=curr_size, errorMessage=None)
    except CalculatorException as e:
        Deps.get_stack_logger(req_metadata.state.request_id).error(f"Server encountered an error ! message: {e.message}")
        return Response(result=None, errorMessage=e.message)

@calc_router.get("/history")
async def get_history(req_metadata: Request, flavor: Optional[str] = None) -> HistoryResponse:
    try:
        res = calculator.get_operations_history(flavor)
        total_actions = len(res)
        if not flavor or flavor == "STACK":
            total_actions = len(calculator.get_operations_history("STACK"))
            Deps.get_stack_logger(req_metadata.state.request_id).info(f"History: So far total {total_actions} stack actions")
        elif flavor == "INDEPENDENT":
            Deps.get_independent_logger(req_metadata.state.request_id).info(f"History: So far total {total_actions} independent actions")
        return HistoryResponse(result=res, errorMessage=None)
    except CalculatorException as e:
        if not flavor or flavor == "STACK":
            Deps.get_stack_logger(req_metadata.state.request_id).error(f"Server encountered an error ! message: {e.message}")
        elif flavor == "INDEPENDENT":
            Deps.get_independent_logger(req_metadata.state.request_id).error(f"Server encountered an error ! message: {e.message}")
        return HistoryResponse(result=None, errorMessage=e.message)
