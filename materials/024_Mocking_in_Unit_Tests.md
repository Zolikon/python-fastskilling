# Mocking in Unit Tests

Mocking is a technique for replacing parts of your system under test with mock objects, allowing you to isolate code and simulate external dependencies. Python's `unittest.mock` module is a powerful tool for this purpose.

## Basic Mock Example

```python
from unittest.mock import Mock
mock = Mock(return_value=42)
print(mock())  # 42
mock.assert_called()
```

## Patching Objects

- Use `patch` as a decorator or context manager to replace objects during a test:

```python
from unittest.mock import patch
import requests

def get_status(url):
    return requests.get(url).status_code

@patch('requests.get')
def test_get_status(mock_get):
    mock_get.return_value.status_code = 200
    assert get_status('http://example.com') == 200

with patch('requests.get') as mock_get:
    mock_get.return_value.status_code = 404
    assert get_status('http://example.com') == 404
```

## Autospeccing and Side Effects

- `autospec=True` ensures mocks match the real API:

  ```python
  @patch('os.remove', autospec=True)
  def test_remove(mock_remove):
      mock_remove('file.txt')
      mock_remove.assert_called_once_with('file.txt')
  ```

- Simulate exceptions with `side_effect`:

  ```python
  mock = Mock(side_effect=ValueError("fail"))
  try:
      mock()
  except ValueError as e:
      print(e)
  ```

## Inspecting Calls

- `mock.call_args`, `mock.call_count`, `mock.assert_called_with(...)`

## Common Pitfalls

- Over-mocking can make tests hard to understand
- Forgetting to stop patches, leading to side effects
- Not using `autospec` can allow invalid calls

Next: Generators and iterators!
