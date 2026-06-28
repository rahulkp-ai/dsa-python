# Setup Guide

## Prerequisites
- Python 3.9 or higher (`python3 --version`)
- pip
- git (for cloning)

## Quick Setup

```bash
git clone https://github.com/yourusername/DSA-Python.git
cd DSA-Python
chmod +x setup.sh && ./setup.sh
source venv/bin/activate
```

## Manual Setup

```bash
python3 -m venv venv
source venv/bin/activate          # Linux/Mac
# venv\Scripts\activate           # Windows

pip install -r requirements.txt
pip install -e .

# Create __init__.py files
find src -type d -exec touch {}/__init__.py \;
find tests -type d -exec touch {}/__init__.py \;
```

## Verify Installation

```bash
python -c "from src.sorting.sorting_algorithms import merge_sort; print(merge_sort([3,1,2]))"
# Expected: [1, 2, 3]
```

## Running Tests

```bash
make test                         # All tests with coverage
make test-unit                    # Unit tests only
pytest tests/ -k "sorting"        # Filter by topic
pytest tests/ -v --tb=short       # Verbose with short tracebacks
```

## Running Benchmarks

```bash
make benchmark                    # All benchmarks
python benchmarks/sorting_benchmark.py
python benchmarks/graph_benchmark.py
python benchmarks/dp_benchmark.py
python benchmarks/memory_benchmark.py
```

## Jupyter Notebooks

```bash
make notebooks
# Opens at http://localhost:8888
```

## CLI

```bash
python -m src.cli.main demo        # Demo all algorithms
python -m src.cli.main demo sort   # Demo sorting only
python -m src.cli.main info        # Show repo statistics
python -m src.cli.main benchmark   # Run benchmarks
```

## Streamlit Dashboard

```bash
make dashboard
# Opens at http://localhost:8501
```

## Common Issues

**ImportError:** Run `pip install -e .` and create `__init__.py` files.

**ModuleNotFoundError:** Ensure you are in the repo root directory.

**Notebook kernel not found:**
```bash
python -m ipykernel install --user --name=dsa-python
```

**Tests fail:**
```bash
pip install --upgrade -r requirements.txt
```
