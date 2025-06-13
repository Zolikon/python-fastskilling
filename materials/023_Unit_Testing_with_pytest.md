# Unit Testing with pytest

`pytest` is a powerful and user-friendly third-party testing framework for Python. It offers a simple syntax, advanced features, and excellent plugin support.

## Installing pytest

```cmd
pip install pytest
```

## Writing and Running Tests

- Test functions must start with `test_`:

  ```python
  def add(a, b):
      return a + b

  def test_add():
      assert add(2, 3) == 5
  ```

- Run all tests in the current directory:
  ```cmd
  pytest
  ```
- Run a specific test file or function:
  ```cmd
  pytest test_math_utils.py
  pytest test_math_utils.py::test_add
  ```

## Advanced Features

- **Fixtures** for setup/teardown:

  ```python
  import pytest

  @pytest.fixture
  def sample_data():
      return [1, 2, 3]

  def test_sum(sample_data):
      assert sum(sample_data) == 6
  ```

- **Parameterization**:
  ```python
  @pytest.mark.parametrize("x,expected", [(2, 4), (3, 9)])
  def test_square(x, expected):
      assert x**2 == expected
  ```
- **Marking/skipping tests**:

  ```python
  import pytest

  @pytest.mark.skip(reason="Not implemented yet")
  def test_future():
      pass
  ```

## Useful CLI Options

- `-v` (verbose), `-x` (stop after first failure), `--maxfail=2`, `--tb=short`
- `--disable-warnings` to suppress warnings

## Common Pitfalls

- Not prefixing test files or functions with `test_`
- Forgetting to install pytest in your environment
- Not using fixtures for setup/teardown

Next: Mocking in unit tests!
