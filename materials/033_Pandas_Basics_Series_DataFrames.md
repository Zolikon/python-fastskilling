# Pandas Basics: Series and DataFrames

Pandas is a powerful library for data analysis and manipulation. It provides two main data structures: Series (1D) and DataFrame (2D).

## Installation

```cmd
pip install pandas
```

## Series

```python
import pandas as pd
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
print(s["b"])  # 20
```

## DataFrame Creation

```python
data = {"name": ["Alice", "Bob"], "age": [25, 30]}
df = pd.DataFrame(data)
print(df)
```

## Reading and Writing Data

```python
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)
```

## Selecting Data

```python
print(df["name"])         # Column
print(df.loc[0])           # Row by label
print(df.iloc[1])          # Row by index
print(df[(df["age"] > 25)])  # Filtering
```

## Basic Operations

```python
print(df.describe())       # Summary statistics
print(df["age"].mean())   # Mean age
print(df.sort_values("age"))
```

## Common Pitfalls

- Using chained indexing (e.g., df["col"][0]) can lead to warnings
- Not handling missing data (see df.isnull())

Next: Advanced Pandas use cases!
