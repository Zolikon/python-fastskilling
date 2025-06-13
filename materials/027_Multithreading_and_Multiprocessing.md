# Multithreading and Multiprocessing

Python provides two primary approaches for concurrent execution: **multithreading** and **multiprocessing**. Each has distinct use cases, APIs, and limitations.

## The Global Interpreter Lock (GIL)

The **Global Interpreter Lock (GIL)** is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This means that, in CPython, even with multiple threads, only one thread executes Python code at a time. As a result, multithreading is limited for CPU-bound tasks but remains effective for I/O-bound operations.

### Recent Changes to the GIL

With the release of **Python 3.12** and ongoing work towards **Python 3.13+**, significant progress has been made to improve or remove the GIL:

- **Python 3.12** introduced optimizations to reduce GIL contention, improving multithreaded performance for some workloads.
- **Python 3.13** (in development) includes an experimental "no-GIL" build, allowing true parallelism with threads. This is not yet the default and may require code changes.
- The **nogil** project, merged into the mainline as an experimental feature, aims to eventually make Python fully GIL-free, enabling better CPU-bound multithreading.

For most users, the GIL still exists in standard Python releases, but future versions may offer GIL-free options for improved concurrency.

## Multithreading

Multithreading enables concurrent execution of tasks within a single process. It's ideal for I/O-bound operations (e.g., network requests, file I/O), but less effective for CPU-bound tasks due to the Global Interpreter Lock (GIL).

### Key APIs

- `threading.Thread`: Create and manage threads.
- `threading.Lock`, `RLock`: Synchronize access to shared resources.
- `threading.Event`, `Condition`, `Semaphore`: Advanced thread coordination.
- `concurrent.futures.ThreadPoolExecutor`: High-level thread pool interface.

### Example: Basic Thread

```python
import threading

def worker(num):
    print(f"Worker {num} running")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
```

### Example: Using a Lock

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)
```

### Example: ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(square, range(5)))
print(results)
```

## Multiprocessing

Multiprocessing allows true parallelism by running code in separate processes, each with its own Python interpreter and memory space. This bypasses the GIL and is suitable for CPU-bound tasks.

### Key APIs

- `multiprocessing.Process`: Create and manage processes.
- `multiprocessing.Pool`: Pool of worker processes for parallel execution.
- `multiprocessing.Queue`, `Pipe`: Inter-process communication.
- `concurrent.futures.ProcessPoolExecutor`: High-level process pool interface.
- `multiprocessing.Manager`: Shared state between processes.

### Example: Basic Process

```python
from multiprocessing import Process

def worker(num):
    print(f"Worker process {num} running")

processes = []
for i in range(3):
    p = Process(target=worker, args=(i,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()
```

### Example: Using a Pool

```python
from multiprocessing import Pool

def cube(n):
    return n ** 3

with Pool(4) as pool:
    results = pool.map(cube, range(5))
print(results)
```

### Example: Shared State with Manager

```python
from multiprocessing import Process, Manager

def worker(shared_list):
    shared_list.append(1)

with Manager() as manager:
    shared = manager.list()
    processes = [Process(target=worker, args=(shared,)) for _ in range(5)]
    for p in processes: p.start()
    for p in processes: p.join()
    print(list(shared))
```

## Common Pitfalls and Considerations

- **Race Conditions**: Threads sharing data must use synchronization primitives to avoid inconsistent state.
- **Deadlocks**: Improper locking can cause threads or processes to wait forever.
- **Overhead**: Multiprocessing has higher startup and communication overhead; use it for CPU-bound or long-running tasks.
- **Data Sharing**: Threads share memory; processes do not. Use `multiprocessing.Manager`, `Queue`, or `Pipe` for inter-process communication.
- **Debugging**: Debugging concurrent code can be challenging due to non-deterministic behavior.

## Further Reading

- [threading — Thread-based parallelism](https://docs.python.org/3/library/threading.html)
- [multiprocessing — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)
- [concurrent.futures — High-level concurrency](https://docs.python.org/3/library/concurrent.futures.html)

**Next:** Performance considerations and best practices for concurrency in Python.
