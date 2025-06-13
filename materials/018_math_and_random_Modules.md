# math and random Modules

These modules provide mathematical functions and random number generation.

## math Module

- Common functions:
  ```python
  import math
  print(math.sqrt(16))      # 4.0
  print(math.pi)            # 3.141592...
  print(math.factorial(5))  # 120
  ```
- Trigonometric functions:
  ```python
  print(math.sin(math.pi / 2))  # 1.0
  ```

## random Module

- Generate random numbers:
  ```python
  import random
  print(random.randint(1, 10))      # Random int between 1 and 10
  print(random.choice(['a', 'b']))  # Randomly pick from list
  ```
- Shuffle a list:
  ```python
  items = [1, 2, 3, 4]
  random.shuffle(items)
  print(items)
  ```

## Common Pitfalls

- Using `random` for cryptographic purposes (use `secrets` instead).
- Forgetting to import the module before use.

Next: Virtual environments!
