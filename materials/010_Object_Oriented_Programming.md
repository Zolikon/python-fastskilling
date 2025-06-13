# Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes. It enables code reuse, modularity, and abstraction by modeling real-world entities as objects.

## Classes and Objects

A **class** is a blueprint for creating objects (instances). An **object** is an instance of a class, encapsulating data (attributes) and behavior (methods).

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute

    def bark(self):
        print(f"{self.name} says woof!")

fido = Dog("Fido")
fido.bark()  # Output: Fido says woof!
```

## Inheritance

**Inheritance** allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass), promoting code reuse.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

whiskers = Cat()
whiskers.speak()  # Output: Meow
```

## Class Decorators: `@staticmethod` and `@classmethod`

- **`@staticmethod`**: Defines a method that does not access the instance (`self`) or class (`cls`). It behaves like a regular function but belongs to the class's namespace.

- **`@classmethod`**: Defines a method that receives the class (`cls`) as its first argument instead of the instance.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"This is {cls.__name__} class."

print(MathUtils.add(2, 3))           # Output: 5
print(MathUtils.description())       # Output: This is MathUtils class.
```

## Special Methods (Magic Methods)

Special methods (also called magic or dunder methods) allow you to define how objects behave with built-in operations.

- `__init__(self, ...)`: Constructor, called when an object is created.
- `__str__(self)`: Defines the string representation (used by `print()`).
- `__repr__(self)`: Defines the official string representation (used in debugging).
- `__eq__(self, other)`: Defines equality comparison (`==`).
- `__len__(self)`: Defines behavior for `len()`.

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book({self.title!r})"

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

book1 = Book("1984")
book2 = Book("1984")
print(book1)              # Output: Book: 1984
print(repr(book1))        # Output: Book('1984')
print(book1 == book2)     # Output: True
```

## Common Pitfalls

- Forgetting to include `self` as the first parameter in instance methods.
- Overriding methods unintentionally due to naming conflicts.
- Not using `super()` when extending methods in subclasses.
- Misusing class and static methods.

---

**Next:** Error handling and exceptions!
