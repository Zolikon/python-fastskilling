# FastAPI Advanced: Middleware, CORS, and Authentication

This lecture covers advanced FastAPI features for building robust APIs, including middleware, CORS, and authentication.

## Middleware

Middleware lets you process requests and responses globally.

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class SimpleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Request path: {request.url.path}")
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "Value"
        return response

app.add_middleware(SimpleMiddleware)
```

## CORS (Cross-Origin Resource Sharing)

CORS allows your API to be called from browsers on other domains.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

## Authentication (OAuth2 Password Flow)

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    if token != "secrettoken":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": "authenticated"}
```

## Dependency Injection

FastAPI's `Depends` lets you inject reusable logic:

```python
from fastapi import Depends

def get_db():
    db = ...  # connect to db
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db=Depends(get_db)):
    return db.query(...)
```

## Custom Exception Handlers

```python
from fastapi.responses import JSONResponse
from fastapi.requests import Request

@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": str(exc)})
```

## Background Tasks

```python
from fastapi import BackgroundTasks

@app.post("/send-email/")
def send_email(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(send_email_func, email)
    return {"message": "Email scheduled"}
```

Explore FastAPI's docs for more advanced features: https://fastapi.tiangolo.com/
