# uv: Usage and Best Practices

## Lecture: uv - A Modern Python Package and Project Manager

### Introduction

**uv** is an extremely fast Python package and project manager, written in Rust and backed by Astral (the creators of Ruff). It aims to unify and accelerate Python development workflows by replacing tools like pip, pip-tools, pipx, poetry, pyenv, twine, and virtualenv with a single, high-performance CLI.

---

### Key Highlights

- **All-in-one tool:** Manages dependencies, environments, Python versions, scripts, and tools.
- **Performance:** 10–100x faster than pip, with disk-space efficient global caching.
- **Universal lockfile:** Ensures reproducible builds across platforms.
- **Script support:** Inline dependency metadata for single-file scripts.
- **Python version management:** Install, pin, and switch between Python versions.
- **Familiar interface:** Drop-in replacement for pip and related tools.
- **Cross-platform:** Works on macOS, Linux, and Windows.
- **No Rust/Python required for install:** Standalone installers available.

---

### Installation

**Standalone installer:**

```sh
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Via PyPI:**

```sh
pip install uv
# or
pipx install uv
```

**Self-update:**

```sh
uv self update
```

---

### Project Management

uv manages project dependencies and environments, supporting lockfiles and workspaces:

```sh
uv init example
cd example
uv add ruff
uv run ruff check
uv lock
uv sync
```

- **Lockfiles:** Ensure consistent, reproducible environments.
- **Workspaces:** Manage multi-package projects (like Cargo).

---

### Script Management

uv can manage dependencies for single-file scripts using inline metadata:

```sh
echo 'import requests; print(requests.get("https://astral.sh"))' > example.py
uv add --script example.py requests
uv run example.py
```

---

### Tool Management

Run or install CLI tools from Python packages:

```sh
uvx pycowsay 'hello world!'   # ephemeral run
uv tool install ruff          # persistent install
ruff --version
```

---

### Python Version Management

Install and switch between multiple Python versions:

```sh
uv python install 3.10 3.11 3.12
uv venv --python 3.12.0
uv run --python pypy@3.8 -- python --version
uv python pin 3.11
```

---

### pip-Compatible Interface

uv provides a drop-in replacement for pip, pip-tools, and virtualenv:

```sh
uv pip compile docs/requirements.in --universal --output-file docs/requirements.txt
uv venv
uv pip sync docs/requirements.txt
```

- **Advanced features:** Dependency version overrides, platform-independent resolutions, reproducible builds.

---

### Documentation and Support

- **Docs:** [docs.astral.sh/uv](https://docs.astral.sh/uv)
- **CLI Reference:** `uv help`
- **Platform support, versioning, and contributing:** See official docs.

---

### FAQ

- **Pronunciation:** "you-vee"
- **Stylization:** Always "uv"

---

### Acknowledgements & License

- **Dependency resolver:** Based on PubGrub.
- **Git implementation:** Inspired by Cargo.
- **Optimizations:** Inspired by pnpm, Orogene, Bun, and Posy.
- **License:** Apache 2.0 or MIT (dual-licensed).

---

### Conclusion

uv is a modern, high-performance tool that streamlines Python development by unifying package management, environment handling, script execution, and Python version management. Its speed, reliability, and comprehensive feature set make it a compelling choice for Python developers seeking efficiency and simplicity.
