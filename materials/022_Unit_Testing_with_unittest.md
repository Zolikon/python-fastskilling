# Unit Testing with unittest

Unit testing is the process of testing individual units of code (like functions or classes) to ensure they work as expected. Python's built-in `unittest` module provides a robust framework for writing and running tests.

## Why Test?

- Catch bugs early
- Make code easier to maintain
- Enable safe refactoring
- Document code behavior

## Basic Test Example

```python
# test_math_utils.py
import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

## Test Discovery and Running

- Run a single test file:

  ```cmd
  python -m unittest test_math_utils.py
  ```

- Discover and run all tests in a directory:

  ```cmd
  python -m unittest discover
  ```

## More Assertions

- `assertTrue(x)` / `assertFalse(x)`
- `assertIn(a, b)` / `assertNotIn(a, b)`
- `assertRaises(Exception, func, *args, **kwargs)`
- `assertIs(a, b)` / `assertIsNot(a, b)`

## Test Fixtures

- `setUp(self)`: Run before each test
- `tearDown(self)`: Run after each test

  ```python
  class MyTest(unittest.TestCase):
      def setUp(self):
          self.data = [1, 2, 3]
      def tearDown(self):
          self.data = None
  ```

## Skipping and Expected Failures

```python
@unittest.skip("demonstrating skipping")
def test_nothing(self):
    pass

@unittest.expectedFailure
def test_fail(self):
    self.assertEqual(1, 0)
```

## Common Pitfalls

- Not following naming conventions (`test_` prefix)
- Tests that depend on each other
- Not cleaning up after tests (use fixtures)

Next: Unit testing with pytest!
