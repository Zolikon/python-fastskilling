# pip: Usage and Best Practices

`pip` is the standard package installer for Python, allowing you to install, upgrade, and manage third-party libraries from the Python Package Index (PyPI) and other sources.

## Installing Packages

- From PyPI:

  ```cmd
  pip install requests
  pip install numpy==1.26.0
  pip install "pandas>=2.0,<3.0"
  ```

- From a requirements file:

  ```cmd
  pip install -r requirements.txt
  ```

- From a local directory or GitHub:

  ```cmd
  pip install ./my_package
  pip install git+https://github.com/psf/requests.git
  ```

## Listing and Searching Packages

- List installed packages:

  ```cmd
  pip list
  ```

- Show outdated packages:

  ```cmd
  pip list --outdated
  ```

- Search PyPI:

  ```cmd
  pip search flask
  ```

## Upgrading and Uninstalling

- Upgrade a package:

  ```cmd
  pip install --upgrade requests
  ```

- Uninstall a package:

  ```cmd
  pip uninstall requests
  ```

## Inspecting Packages

- Show package info:

  ```cmd
  pip show requests
  ```

- Show install location:

  ```cmd
  pip show -f requests
  ```

## Using Installed Packages

```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

## Common Pitfalls

- Not using a virtual environment (can pollute global Python)
- Version conflicts between packages
- Forgetting to update `requirements.txt` after installing new packages
- Installing packages as admin/root (use user installs or venvs)

## Best Practices

- Always use a virtual environment
- Use `pip freeze > requirements.txt` to record dependencies
- Use `pip check` to detect dependency conflicts

Next: uv usage and best practices!
