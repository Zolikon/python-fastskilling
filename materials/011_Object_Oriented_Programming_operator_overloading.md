# OOP - operator overloading

Operator overloading in Python allows classes to define or extend the meaning of standard operators (such as `+`, `-`, `*`, `==`, etc.) when they are used with class instances. This is achieved by implementing special methods (also called "magic methods") in your class. These methods have names that begin and end with double underscores, such as `__add__` for addition or `__eq__` for equality comparison.

## Why Use Operator Overloading?

Operator overloading makes user-defined objects behave more like built-in types, improving code readability and intuitiveness. For example, you can add two `Point` objects using `+`, or compare two `Vector` objects using `==`.

## How Operator Overloading Works

When you use an operator with objects, Python internally calls the corresponding special method. For example, `a + b` calls `a.__add__(b)`. If the method is not defined, Python raises a `TypeError`.

## Example 1: Overloading the `+` Operator (`__add__`)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

## Example 2: Overloading the `*` Operator (`__mul__`)

```python
class ScalarMultiplier:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ScalarMultiplier(self.value * other)
        return NotImplemented

    def __repr__(self):
        return f"ScalarMultiplier({self.value})"

a = ScalarMultiplier(5)
print(a * 3)  # Output: ScalarMultiplier(15)
```

## Example 3: Overloading the Equality Operator (`__eq__`)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1 == p2)  # Output: True
```

## Example 4: Overloading the Indexing Operator (`__getitem__`)

```python
class CustomList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index] ** 2  # Returns the square of the item

lst = CustomList([1, 2, 3])
print(lst[1])  # Output: 4
```

## Example 5: Overloading the String Representation (`__str__`)

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python 101")
print(str(b))  # Output: Book: Python 101
```

## Notes

- If the argument to an operator is not of the expected type, return `NotImplemented` to allow Python to try the reflected operation or raise an appropriate error.
- You can overload many operators, including arithmetic (`+`, `-`, `*`, `/`), comparison (`==`, `<`, `>`), and others like indexing (`[]`) and string conversion (`str()`).

For a full list of special methods, see the [Python data model documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names).
