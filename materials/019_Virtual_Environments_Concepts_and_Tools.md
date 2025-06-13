# Virtual Environments: Concepts and Tools

Virtual environments are isolated Python environments that allow you to manage dependencies for each project separately. This prevents conflicts between packages and keeps your global Python installation clean.

## Why Use Virtual Environments?

- Avoid dependency conflicts between projects
- Reproducible environments for development, testing, and deployment
- Safe experimentation with package versions

## Built-in venv Module

### Creating a Virtual Environment

```cmd
python -m venv .venv
```

This creates a `.venv` directory containing a fresh Python environment.

### Activating the Environment

- **Windows:**

  ```cmd
  .venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source .venv/bin/activate
  ```

### Deactivating the Environment

```cmd
deactivate
```

### Removing a Virtual Environment

Simply delete the `.venv` directory:

```cmd
rmdir /s /q .venv
```

## Using virtualenv (Alternative Tool)

`virtualenv` is an older, widely used tool with more options:

```cmd
pip install virtualenv
virtualenv venv_alt
venv_alt\Scripts\activate
```

## Inspecting the Environment

- List installed packages:

  ```cmd
  pip list
  ```

- Show the Python executable:

  ```python
  import sys
  print(sys.executable)
  ```

## Common Pitfalls

- Forgetting to activate the environment before installing packages (installs globally!)
- Accidentally using the wrong Python interpreter
- Not including a `requirements.txt` for reproducibility

## Best Practices

- Use a virtual environment for every project
- Store dependencies in `requirements.txt`:

  ```cmd
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```

Next: pip usage and best practices!
