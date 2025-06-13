# datetime and time Modules

The `datetime` and `time` modules in Python provide powerful tools for manipulating dates, times, and time intervals. These modules are essential for tasks such as logging, scheduling, and time-based calculations.

---

## `datetime` Module

The `datetime` module supplies classes for manipulating dates and times in both simple and complex ways.

### Getting Current Date and Time

```python
from datetime import datetime, date, time

now = datetime.now()          # Current date and time
today = date.today()          # Current date
current_time = datetime.now().time()  # Current time

print("Now:", now)
print("Today:", today)
print("Current Time:", current_time)
```

### Creating Specific Dates and Times

```python
from datetime import datetime, date, time

dt = datetime(2024, 6, 7, 15, 30, 0)
d = date(2024, 6, 7)
t = time(15, 30, 0)

print("Datetime:", dt)
print("Date:", d)
print("Time:", t)
```

### Formatting Dates and Times

```python
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-06-07 15:30:00
print(now.strftime("%A, %B %d, %Y"))      # Friday, June 07, 2024
```

### Parsing Strings to Dates

```python
from datetime import datetime

dt = datetime.strptime("2025-06-07 14:45", "%Y-%m-%d %H:%M")
print(dt)
```

### Date Arithmetic

```python
from datetime import datetime, timedelta

now = datetime.now()
one_week = timedelta(weeks=1)
future = now + one_week
past = now - timedelta(days=3)

print("One week from now:", future)
print("Three days ago:", past)
```

### Working with Time Zones

```python
from datetime import datetime, timezone, timedelta

utc_now = datetime.now(timezone.utc)
local = utc_now.astimezone()  # Convert to local time

print("UTC Now:", utc_now)
print("Local Time:", local)
```

---

## `time` Module

The `time` module provides functions for working with time, measuring intervals, and sleeping.

### Sleeping

```python
import time

print("Sleeping for 2 seconds...")
time.sleep(2)
print("Done sleeping!")
```

### Measuring Elapsed Time

```python
import time

start = time.time()
# ... some code ...
end = time.time()
print(f"Elapsed: {end - start:.2f} seconds")
```

### Getting Current Time

```python
import time

print("Epoch time:", time.time())
print("Local time struct:", time.localtime())
print("Formatted:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
```

---

## Common Pitfalls

- **Time Zones:** The standard library's `datetime` module has limited timezone support. For robust timezone handling, use `zoneinfo` (Python 3.9+) or third-party libraries like `pytz`.
- **Naive vs. Aware Objects:** Naive datetime objects lack timezone info. Mixing naive and aware objects can cause errors.
- **Leap Seconds:** The `time` module does not account for leap seconds.
- **Locale Issues:** Formatting and parsing can be locale-dependent.

---

**Next:** [math and random modules](#)
