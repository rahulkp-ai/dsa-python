# Contributing to DSA-Python

Thank you for contributing! Every algorithm, fix, and improvement makes this resource better.

## 🚀 How to Contribute

### 1. Fork & Clone
```bash
git clone https://github.com/yourusername/DSA-Python.git
cd DSA-Python
git checkout -b feature/algorithm-name
```

### 2. Setup
```bash
./setup.sh && source venv/bin/activate
```

### 3. Algorithm File Template
```python
"""
Module: algorithm_name.py
Topic: Category (Sorting / Graphs / DP / ...)

Problem Statement:
    Description of what the algorithm solves.

Time Complexity:  O(...)
Space Complexity: O(...)
"""
from typing import List, Optional


def my_algorithm(nums: List[int], target: int) -> int:
    """
    Brief one-line description.

    Args:
        nums: Input list of integers.
        target: Target value.

    Returns:
        Result description.

    Raises:
        ValueError: If input is invalid.

    Examples:
        >>> my_algorithm([1, 2, 3], 2)
        1

    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    # Implementation
    pass


if __name__ == "__main__":
    result = my_algorithm([1, 2, 3], 2)
    print(f"Result: {result}")
```

### 4. Add Tests
```python
# tests/unit/test_my_algorithm.py
def test_normal_case():
    assert my_algorithm([1,2,3], 2) == 1

def test_empty_input():
    assert my_algorithm([], 0) == -1

def test_edge_case():
    assert my_algorithm([5], 5) == 0
```

### 5. Check & Submit
```bash
make format && make lint && make test
git push origin feature/algorithm-name
# Open Pull Request
```

## 📋 Standards

- **PEP8** compliance (max line length 88)
- **Type hints** on all function signatures
- **Google-style docstrings** with complexity analysis
- **Minimum 3 test cases**: normal, empty/edge, stress

## 🐛 Reporting Bugs

Use GitHub Issues with the bug report template.

## 💡 Requesting Features

Use GitHub Issues with the feature request template.
