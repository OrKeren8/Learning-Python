from loguru import logger
import os

os.makedirs("logs", exist_ok=True)

class Deps():
    logger.remove()
    logger.add(
        "logs/request.log",
        rotation="10 MB",
        level="DEBUG",
        format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
        filter=lambda r: r["extra"].get("name") == "request_logger"
    )
    logger.add( 
        "logs/stack.log",
        rotation="10 MB",
        level="DEBUG",
        format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
        filter=lambda r: r["extra"].get("name") == "stack_logger"
    )
    logger.add( 
        "logs/independent.log",
        rotation="10 MB",
        level="DEBUG",
        format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
        filter=lambda r: r["extra"].get("name") == "independent_logger"
    )
    
    __req_counter = 1

    @staticmethod
    def req_counter():
        curr_req_counter = Deps.__req_counter
        Deps.__req_counter += 1
        return curr_req_counter
    
    @staticmethod
    def get_req_logger():
        req_idx = Deps.req_counter()        
        return logger.bind(name="request_logger", req_number=req_idx), req_idx
    
    @staticmethod
    def get_stack_logger(req_idx: int):
        return logger.bind(name="stack_logger", req_number=req_idx)
    
    @staticmethod
    def get_independent_logger(req_idx: int):
        return logger.bind(name="independent_logger", req_number=req_idx)