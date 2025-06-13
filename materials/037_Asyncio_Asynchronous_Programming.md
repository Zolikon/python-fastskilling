# Asyncio: Asynchronous Programming in Python

Asyncio is Python's built-in library for writing concurrent code using the async/await syntax. It is ideal for I/O-bound and high-level structured network code, such as web servers, clients, and real-time applications.

## Why Use Asyncio?

- Efficiently handle many I/O-bound tasks (HTTP requests, file/network I/O)
- Avoid blocking the main thread
- Write scalable, high-performance applications

## Basic Concepts

- **Coroutine:** A function defined with `async def` that can be paused and resumed.
- **Event Loop:** The core of asyncio, runs and manages coroutines.
- **Task:** A wrapper for a coroutine, scheduled to run on the event loop.

## Basic Example: Coroutine and Event Loop

```python
import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("...World!")

asyncio.run(say_hello())
```

## Running Multiple Coroutines Concurrently

```python
import asyncio

async def count(n):
    for i in range(n):
        print(f"Count: {i}")
        await asyncio.sleep(0.5)

async def main():
    await asyncio.gather(count(3), count(2))

asyncio.run(main())
```

## Creating and Managing Tasks

```python
import asyncio

async def do_work(x):
    await asyncio.sleep(x)
    return x

async def main():
    task1 = asyncio.create_task(do_work(1))
    task2 = asyncio.create_task(do_work(2))
    result1 = await task1
    result2 = await task2
    print(result1, result2)

asyncio.run(main())
```

## Async Context Managers and Iterators

```python
import asyncio

class AsyncContext:
    async def __aenter__(self):
        print("Entering context")
        return self
    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting context")

async def main():
    async with AsyncContext():
        print("Inside context")

asyncio.run(main())
```

## Making HTTP Requests Asynchronously

```python
import asyncio
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        print(resp.status_code, url)

async def main():
    await asyncio.gather(
        fetch('https://example.com'),
        fetch('https://httpbin.org/get')
    )

asyncio.run(main())
```

## Error Handling in Async Code

```python
import asyncio

async def fail():
    raise ValueError("Oops!")

async def main():
    try:
        await fail()
    except ValueError as e:
        print(f"Caught: {e}")

asyncio.run(main())
```

## Common Pitfalls

- Blocking the event loop with synchronous code (use only async I/O inside coroutines)
- Forgetting to await coroutines
- Using `asyncio.run()` inside an already running event loop (e.g., in Jupyter)

Asyncio is essential for modern, scalable Python applications that need to handle many concurrent I/O operations efficiently.
