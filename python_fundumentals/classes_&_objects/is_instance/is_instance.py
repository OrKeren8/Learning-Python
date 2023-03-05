from abc import ABC, abstractmethod


class SerialException(ABC, Exception):
    """class
    """
    @abstractmethod
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class UartError(SerialException):
    """class"""
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

# x = UartError()

def raise_error():
    """raise exception"""
    raise UartError("momom")

# print(isinstance(x, /SerialException))

try:
    raise_error()

except Exception as e:
    print(e)
    print(type(e))
    print(isinstance(e, SerialException))
    
# except SerialException as e:
#     print('momo')

# except Exception as e:
#     print('koko')
    