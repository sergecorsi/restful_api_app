from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.routers import auth, tasks
from app.config import settings

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

@app.get("/")
@limiter.limit("100/minute")
def read_root(request: Request):
    return {"message": "Hello"}
