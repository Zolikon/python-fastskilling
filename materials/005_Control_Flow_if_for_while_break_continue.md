# Control Flow: if, for, while, break, continue

Control flow statements determine the sequence in which your code runs, allowing you to make decisions and repeat actions.

## Conditional Statements (`if`, `elif`, `else`)

Conditional statements let you execute code blocks based on whether a condition is `True` or `False`.

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

- `if` checks the first condition.
- `elif` (else if) checks another condition if the previous ones were `False`.
- `else` runs if none of the above conditions are `True`.

## Loops

Loops let you repeat code multiple times.

### for loop

A `for` loop iterates over a sequence (like a list or a range of numbers):

```python
for i in range(3):
    print(i)
```

- This prints numbers 0, 1, and 2.

> **Note:**  
> `range(n)` generates a sequence of numbers from 0 up to (but not including) `n`. It's commonly used for looping a specific number of times.

### while loop

A `while` loop repeats as long as a condition is `True`:

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

- This prints numbers 0, 1, and 2, incrementing `count` each time.

## Loop Control: `break` and `continue`

- `break` immediately exits the loop, even if the condition is still `True`.
- `continue` skips the rest of the current loop iteration and moves to the next one.

```python
for i in range(5):
    if i == 3:
        break  # Stops the loop when i is 3
    print(i)
```

```python
for i in range(5):
    if i == 2:
        continue  # Skips printing when i is 2
    print(i)
```

## Common Pitfalls

- **Infinite loops:** Forgetting to update the loop variable or incorrect conditions can cause loops to run forever.
- **Off-by-one errors:** Misunderstanding how `range` works can lead to missing or extra iterations.

---

Next, you'll learn about defining and using functions in Python!
