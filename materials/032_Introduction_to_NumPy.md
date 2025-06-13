# Introduction to NumPy

NumPy is the fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them efficiently.

## Installation

```cmd
pip install numpy
```

## Creating Arrays

```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr)
# 2D array
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
```

## Array Properties

```python
print(arr.shape)      # (3,)
print(matrix.shape)   # (2, 2)
print(arr.dtype)      # int64 (platform dependent)
```

## Array Operations

```python
print(arr + 10)       # [11 12 13]
print(arr * 2)        # [2 4 6]
print(arr.sum())      # 6
print(matrix.T)       # Transpose
```

## Indexing and Slicing

```python
print(arr[1])         # 2
print(matrix[0, 1])   # 2
print(arr[1:])        # [2 3]
```

## Broadcasting

```python
b = np.array([10, 20, 30])
print(arr + b)        # [11 22 33]
```

## Common Pitfalls

- Mixing Python lists and NumPy arrays in operations
- Forgetting that NumPy arrays are zero-indexed

NumPy is the foundation for most data science and machine learning workflows in Python.

Next: Pandas basics!
