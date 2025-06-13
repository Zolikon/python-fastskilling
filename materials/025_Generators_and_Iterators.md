# Generators and Iterators

Generators and iterators are powerful tools in Python for working with sequences of data, especially when dealing with large datasets or streams where loading everything into memory is impractical.

## What Are Iterators?

An **iterator** is any object that implements the iterator protocol, consisting of the `__iter__()` and `__next__()` methods. Iterators allow you to traverse through all the elements of a collection, one element at a time.

### Creating and Using Iterators

Most built-in Python collections (like lists, tuples, and dictionaries) are iterable, meaning you can obtain an iterator from them using the `iter()` function.

```python
nums = [10, 20, 30]
iterator = iter(nums)
print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
# next(iterator) would raise StopIteration
```

You can also create your own iterator by defining a class with `__iter__()` and `__next__()`:

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(3):
    print(num)  # 3, 2, 1
```

## Generator Functions

A **generator function** is a special type of function that uses the `yield` statement to return values one at a time, suspending and resuming its state between each value.

### Example: Simple Generator

```python
def simple_gen():
    yield 'a'
    yield 'b'
    yield 'c'

for value in simple_gen():
    print(value)
```

### Example: Infinite Generator

Generators can produce infinite sequences:

```python
def infinite_counter():
    n = 1
    while True:
        yield n
        n += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))  # 1, 2, 3, 4, 5
```

## Generator Expressions

**Generator expressions** are similar to list comprehensions, but use parentheses and produce items lazily (one at a time).

```python
squares = (x**2 for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
for sq in squares:
    print(sq)  # 4, 9, 16
```

## Why Use Generators and Iterators?

- **Memory efficiency:** Only one item is in memory at a time.
- **Representing infinite sequences:** Useful for streams or data pipelines.
- **Composability:** Generators can be chained together.

## Common Pitfalls

- **Exhaustion:** Once an iterator or generator is exhausted, it cannot be reused.
- **Forgetting `yield`:** Omitting `yield` in a generator function makes it a normal function.
- **StopIteration:** Calling `next()` after exhaustion raises `StopIteration`.

## More Examples

### Chaining Generators

```python
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def squared(seq):
    for num in seq:
        yield num ** 2

for val in squared(even_numbers(6)):
    print(val)  # 0, 4, 16
```

### Using `itertools` for Advanced Iteration

```python
import itertools

# Infinite counting
for num in itertools.count(10, 2):
    if num > 16:
        break
    print(num)  # 10, 12, 14, 16
```

---

Next: Decorators!
