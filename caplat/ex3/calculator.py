from typing import Optional
from exceptions import DivisionByZeroError, FactOfMinusError, InputError
from models import CalculateRequest
from collections import deque



class Calculator:

    def __init__(self):
        self._stack = deque()

    @property
    def stack_size(self) -> int:
        return len(self._stack)
    
    def get_stack_args(self, count: int) -> list:
        if count > len(self._stack):
            raise InputError(f"{count}")
        args = [self._stack.pop() for _ in range(count)]
        return args

    def calculate_from_stack(self, operation: str) -> int:
        args_count = 1 if operation.lower() == 'abs' else 2
        try:
            args = self.get_stack_args(args_count)
        except InputError as e:
            raise InputError(f"Error: cannot implement operation {operation}. It requires {e.message} arguments and the stack has only {self.stack_size} arguments")
        req = CalculateRequest(arguments=args, operation=operation)
        return self.calculate(req)

    def calculate(self, req: Optional[CalculateRequest] = None) -> int:
        operations = {
            'plus': self.add,
            'minus': self.subtract,
            'times': self.multiply,
            'divide': self.divide,
            'pow': self.pow,
            'abs': self.absolute,
            'fact': self.factorial
        }
        try:
            func = operations[req.operation.lower()]
        except KeyError:
            raise InputError(f"unknown operation: {req.operation}")
        arg_count = func.__code__.co_argcount - 1  # subtract self
        if arg_count > len(req.arguments):
            raise InputError(f"Not enough arguments to perform the operation {req.operation}")
        elif arg_count < len(req.arguments):
            raise InputError(f"Too many arguments to perform the operation {req.operation}")
        return func(*req.arguments)
        
    def add(self, x: int, y: int) -> int:
        return x + y

    def subtract(self, x: int, y: int) -> int:
        return x - y

    def multiply(self, x: int, y: int) -> int:
        return x * y

    def divide(self, x: int, y: int) -> int:
        if y == 0:
            raise DivisionByZeroError()
        return x // y

    def pow(self, x: int, y: int) -> int:
        return x ** y
    
    def absolute(self, x: int) -> int:
        return abs(x)
    
    def factorial(self, x: int) -> int:
        if x < 0:
            raise FactOfMinusError()
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
