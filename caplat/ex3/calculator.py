from exceptions import DivisionByZeroError, FactOfMinusError
from models import CalculateRequest


class Calculator:

    @staticmethod
    def calculate(req: CalculateRequest) -> int:
        operations = {
            'add': Calculator.add,
            'subtract': Calculator.subtract,
            'multiply': Calculator.multiply,
            'divide': Calculator.divide,
            'pow': Calculator.pow,
            'absolute': Calculator.absolute,
            'factorial': Calculator.factorial
        }
        return operations[req.operation](*req.arguments)

    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y

    @staticmethod
    def subtract(x: int, y: int) -> int:
        return x - y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        return x * y

    @staticmethod
    def divide(x: int, y: int) -> int:
        if y == 0:
            raise DivisionByZeroError()
        return x // y

    @staticmethod
    def pow(x: int, y: int) -> int:
        return x ** y
    
    @staticmethod
    def absolute(x: int) -> int:
        return abs(x)
    
    @staticmethod
    def factorial(x: int) -> int:
        if x < 0:
            raise FactOfMinusError()
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result