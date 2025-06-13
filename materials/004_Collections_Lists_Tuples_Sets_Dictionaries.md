# Collections: Lists, Tuples, Sets, Dictionaries

Python provides several built-in collection types for storing groups of items.

## Lists

Lists are ordered, mutable sequences that can hold elements of any type. You can add, remove, or modify items after creation. Lists support indexing, slicing, and many useful methods.

**Examples:**

```python
# Creating a list
numbers = [1, 2, 3, 4]

# Adding elements
numbers.append(5)         # [1, 2, 3, 4, 5]
numbers.insert(1, 10)     # [1, 10, 2, 3, 4, 5]

# Removing elements
numbers.remove(3)         # [1, 10, 2, 4, 5]
popped = numbers.pop()    # popped = 5, numbers = [1, 10, 2, 4]

# Accessing elements
first = numbers[0]        # 1
slice = numbers[1:3]      # [10, 2]
last = numbers[-1]        # 4 (last element)
first_two = numbers[:2]   # [1, 10]
every_other = numbers[::2]# [1, 2]
reversed_list = numbers[::-1]  # [4, 2, 10, 1]
```

## Tuples

Tuples are ordered, immutable sequences. Once created, their contents cannot be changed. Tuples are often used to group related data. For a tuple with a single element, a trailing comma is required.

**Examples:**

```python
# Creating tuples
coordinates = (10, 20)
empty_tuple = ()
single_element = (5,)  # Note the comma

# Accessing elements
x = coordinates[0]     # 10

# Tuple unpacking
a, b = coordinates     # a = 10, b = 20

# Concatenation
combined = coordinates + (30, 40)  # (10, 20, 30, 40)
```

## Sets

Sets are unordered collections of unique, immutable elements. They are useful for membership tests, removing duplicates, and set operations like union and intersection.

**Examples:**

```python
# Creating a set
animals = {"cat", "dog", "bird"}

# Adding and removing elements
animals.add("fish")
animals.discard("dog")

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b         # {1, 2, 3, 4, 5}
intersection = a & b  # {3}
difference = a - b    # {1, 2}
```

## Dictionaries

Dictionaries are unordered collections of key-value pairs. Keys must be unique and immutable (such as strings, numbers, or tuples), while values can be of any type. Dictionaries are mutable, allowing you to add, modify, or remove key-value pairs after creation.

**Examples:**

```python
# Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values
name = person["name"]         # "Alice"

# Adding or updating entries
person["email"] = "alice@example.com"
person["age"] = 31            # Updates the value for "age"

# Removing entries
del person["city"]

# Iterating over keys and values
for key, value in person.items():
    print(key, value)

# Checking for a key
if "email" in person:
    print("Email found!")

# Dictionary methods
keys = list(person.keys())    # ["name", "age", "email"]
values = list(person.values())# ["Alice", 31, "alice@example.com"]
items = list(person.items())  # [("name", "Alice"), ("age", 31), ("email", "alice@example.com")]
```

Dictionaries are highly efficient for lookups, insertions, and deletions by key. They are commonly used for storing structured data, configuration, and mapping relationships.

## Common Pitfalls

- Modifying a list while iterating over it can cause unexpected behavior.
- Using mutable objects as dictionary keys is not allowed.
  Next, learn about control flow in Python!
