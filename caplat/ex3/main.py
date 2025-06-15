from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from router import calc_router
import uvicorn
from deps import Deps
from timeit import default_timer as timer
import timeit

app = FastAPI()

app.include_router(calc_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    req_log, req_idx = Deps.get_req_logger()
    request.state.request_id = req_idx
    path = request.url.path
    method = request.method.upper()
    req_log.info(f"Incoming request | #{req_idx} | resource: {path} | HTTP Verb {method}")
    st = timer()
    response = await call_next(request)
    duration = int((timer() - st) * 1000)
    req_log.debug(f"request #{req_idx} duration: {duration}ms")
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8496)