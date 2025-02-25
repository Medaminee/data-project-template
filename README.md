# Python data project Template 🐍

A template for a data python project for 2025

Features:
- [x] 📦 [`uv`](https://docs.astral.sh/uv/) as package manager
- [x] 💅 [`ruff`](https://docs.astral.sh/ruff/) for linting and formatting
- [x] 🧪 [`pytest`](https://docs.pytest.org/en/stable/)
- [x] 📚 [`sphinx`](https://www.sphinx-doc.org/en/master/) auto doc generation via 

## Getting started

### Installation

To set it up and run

```bash
uv sync
```

Then

```bash
uv run main.py
```

Will output:
summary statistics of the sample data file.
The dataframe of the people older than 30.
Age distribution in the sample data file. 

### Linting

```
uv run ruff check
```


### Formatting

```
uv run ruff format
```

### Tests
```
uv run pytest
```