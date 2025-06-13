# Advanced Pandas: Data Manipulation and Analysis

This lecture covers more advanced pandas features for real-world data analysis, including merging, grouping, reshaping, and handling missing data.

## Merging and Joining

```python
import pandas as pd
df1 = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"id": [1, 2], "score": [90, 85]})
merged = pd.merge(df1, df2, on="id")
print(merged)
```

## GroupBy and Aggregation

```python
df = pd.DataFrame({"team": ["A", "A", "B"], "score": [10, 20, 30]})
grouped = df.groupby("team")["score"].sum()
print(grouped)
```

## Pivot Tables

```python
df = pd.DataFrame({"team": ["A", "A", "B"], "year": [2020, 2021, 2020], "score": [10, 20, 30]})
pivot = df.pivot_table(index="team", columns="year", values="score", aggfunc="sum")
print(pivot)
```

## Handling Missing Data

```python
df = pd.DataFrame({"a": [1, None, 3]})
print(df.isnull())
df_filled = df.fillna(0)
print(df_filled)
df_dropped = df.dropna()
print(df_dropped)
```

## Reshaping Data

```python
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.melt())
print(df.stack())
```

## Applying Functions

```python
df = pd.DataFrame({"x": [1, 2, 3]})
print(df["x"].apply(lambda v: v ** 2))
```

## Time Series

```python
dates = pd.date_range("2025-01-01", periods=3)
df = pd.DataFrame({"date": dates, "value": [1, 2, 3]})
df.set_index("date", inplace=True)
print(df.resample("D").mean())
```

## Common Pitfalls

- Not resetting index after groupby or pivot
- Not copying data when needed (use df.copy())

Pandas is essential for data science, analytics, and ETL workflows in Python.
