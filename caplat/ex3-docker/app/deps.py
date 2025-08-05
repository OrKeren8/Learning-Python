from loguru import logger
import os

os.makedirs("logs", exist_ok=True)

class Deps():
    logger.remove()
    rlfs = logger.add(
        "logs/request.log",
        rotation="10 MB",
        level="INFO",
        format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
        filter=lambda r: r["extra"].get("name") == "request_logger"
    )
    slfs = logger.add( 
        "logs/stack.log",
        rotation="10 MB",
        level="INFO",
        format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
        filter=lambda r: r["extra"].get("name") == "stack_logger"
    )
    ilfs = logger.add( 
        "logs/independent.log",
        rotation="10 MB",
        level="INFO",
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
    
    @staticmethod
    def get_log_level(logger_name: str):
        return logger.bind(name=logger_name).level
    
    @staticmethod
    def set_log_level(logger_name: str, level: str):
        match logger_name:
            case "request-logger":
                logger.remove(Deps.rlfs)        
                Deps.rlfs = logger.add(
                    "logs/request.log",
                    rotation="10 MB",
                    level=level,
                    format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
                    filter=lambda r: r["extra"].get("name") == "request_logger"
                )
            case "stack-logger":
                logger.remove(Deps.slfs)
                Deps.slfs = logger.add(
                    "logs/stack.log",
                    rotation="10 MB",
                    level=level,
                    format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
                    filter=lambda r: r["extra"].get("name") == "stack_logger"
                )
            case "independent-logger":
                logger.remove(Deps.ilfs)
                Deps.ilfs = logger.add(
                    "logs/independent.log",
                    rotation="10 MB",
                    level=level,
                    format="{time:DD-MM-YYYY HH:mm:ss.SSS} {level}: {message} | request #{extra[req_number]}",
                    filter=lambda r: r["extra"].get("name") == "independent_logger"
                )
            case _:
                raise ValueError(f"Unknown logger name: {logger_name}")
        