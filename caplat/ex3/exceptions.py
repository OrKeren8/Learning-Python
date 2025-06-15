from models import Response

class CalculatorException(Exception):
    def __init__(self, message=None, status_code=500):
        self.message = message
        self.status_code = status_code
        
        super().__init__(message)

class DivisionByZeroError(CalculatorException):
    def __init__(self):
        super().__init__("Error while performing operation Divide: division by 0", status_code=409)

class FactOfMinusError(CalculatorException):
    def __init__(self):
        super().__init__("Error while performing operation Factorial: not supported for the negative number", status_code=409)

class InputError(CalculatorException):
    def __init__(self, msg):
        super().__init__(msg, status_code=409)