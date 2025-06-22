from fastapi import APIRouter, Request, Query

from deps import Deps


logs_router = APIRouter(prefix="/logs")

@logs_router.get("/level")
async def root(logger_name: str = Query(..., alias="logger-name")):
    logger_name = logger_name.lower()
    try:
        level = Deps.get_log_level(logger_name)
        return level.upper()
    except Exception as e:
        return f"Error retrieving log level: {logger_name}"

@logs_router.put("/level")
async def independent_calculation(logger_name: str = Query(..., alias="logger-name"), logger_level: str = Query(..., alias="logger-level")):
    logger_name = logger_name.lower()
    logger_level = logger_level.upper()
    try:
        Deps.set_log_level(logger_name, logger_level)
        return logger_level
    except Exception as e:
        return f"Error setting log level for {logger_name}: {str(e)}"