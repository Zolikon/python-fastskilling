# FastAPI Basics: Building REST APIs

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is widely used for building RESTful APIs due to its speed, automatic documentation, and ease of use.

## Installation

```cmd
pip install fastapi uvicorn
```

## Installation

```cmd
pip install fastapi uvicorn
```

**What is Uvicorn and why is it needed?**

Uvicorn is a lightning-fast ASGI(Asynchronous Server Gateway Interface) server implementation, using `uvloop` and `httptools`. FastAPI itself is just a framework for building APIs; it doesn't serve HTTP requests directly. Uvicorn acts as the server that runs your FastAPI application, handling incoming HTTP requests and sending responses. Without Uvicorn (or another ASGI server), your FastAPI app can't receive or respond to web traffic.

## Creating a Simple FastAPI App

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

## Running the App

```cmd
uvicorn main:app --reload
```

## Path Parameters

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

## Query Parameters

```python
@app.get("/search/")
def search(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}
```

## Request Body (POST)

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

## Headers

```python
from fastapi import Header

@app.get("/header-demo/")
def header_demo(user_agent: str = Header(None)):
    return {"User-Agent": user_agent}
```

## Automatic Docs

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

FastAPI automatically generates interactive API documentation.

Next: Advanced FastAPI (middlewares, CORS, authentication, and more)!
