# Comprehensions: List, Dict, Set, Nested

Comprehensions in Python are powerful tools for creating new lists, dictionaries, or sets from existing iterables in a clear and concise way. They allow you to replace verbose loops with a single line of code, making your programs more readable and expressive.

## What Are Comprehensions?

Comprehensions are syntactic constructs that let you generate collections by specifying the elements and the rules for including them. There are three main types:

- **List comprehensions**
- **Dictionary comprehensions**
- **Set comprehensions**

Each type follows a similar pattern, but produces a different kind of collection.

---

## List Comprehensions

List comprehensions create new lists by applying an expression to each item in an iterable.

**Basic Example:**

```python
squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]
```

**With Condition:**

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# Output: [0, 4, 16, 36, 64]
```

---

## Dictionary Comprehensions

Dictionary comprehensions let you build dictionaries by specifying keys and values.

**Example:**

```python
squared_map = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**With Condition:**

```python
even_squared_map = {x: x**2 for x in range(10) if x % 2 == 0}
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

## Set Comprehensions

Set comprehensions create sets, which are unordered collections of unique elements.

**Example:**

```python
unique_lengths = {len(word) for word in ["apple", "banana", "pear"]}
# Output: {4, 5, 6}
```

**With Condition:**

```python
lengths_over_4 = {len(word) for word in ["apple", "banana", "pear"] if len(word) > 4}
# Output: {5, 6}
```

---

## Nested Comprehensions

Nested comprehensions are comprehensions inside comprehensions. They are useful for flattening lists or working with multi-dimensional data.

**Flattening a Matrix:**

```python
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
# Output: [1, 2, 3, 4]
```

**Transposing a Matrix:**

```python
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# Output: [[1, 4], [2, 5], [3, 6]]
```

**Filtering in Nested Comprehensions:**

```python
matrix = [[1, 2, 3], [4, 5, 6]]
evens = [num for row in matrix for num in row if num % 2 == 0]
# Output: [2, 4, 6]
```

### How to Understand Nested Comprehensions

Nested comprehensions can be read from left to right, just like nested loops:

```python
flattened = [num for row in matrix for num in row]
```

This is equivalent to:

```python
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
```

**Tip:** Start from the leftmost `for` and work your way right, just as you would with nested loops.

---

## Common Pitfalls

- **Readability:** Deeply nested comprehensions can be hard to read. If a comprehension is too complex, consider using regular loops.
- **Side Effects:** Avoid using comprehensions for side effects (like printing or modifying external variables).
- **Memory Usage:** Large comprehensions can consume a lot of memory. Use generator expressions (`()` instead of `[]`) when possible for large datasets.

---

Comprehensions are a concise and expressive way to work with collections in Python. Practice with different examples to become comfortable with their syntax and power.

Next: Modules and packages!

Comprehensions provide a concise way to create collections.

## List Comprehensions

```python
squares = [x**2 for x in range(5)]
```

## Dictionary Comprehensions

```python
squared_map = {x: x**2 for x in range(5)}
```

## Set Comprehensions

```python
unique_lengths = {len(word) for word in ["apple", "banana", "pear"]}
```

## Nested Comprehensions

```python
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
```

## Common Pitfalls

- Nested comprehensions can reduce readability.
- Avoid using comprehensions for side effects.

Next: Modules and packages!
