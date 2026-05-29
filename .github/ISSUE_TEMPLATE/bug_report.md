---
name: Bug Report
about: Report a bug or incorrect implementation
labels: bug
---

**Algorithm/Module:** e.g., `src/sorting/sorting_algorithms.py`

**Describe the bug:**
A clear description of what the bug is.

**To Reproduce:**
```python
from src.sorting.sorting_algorithms import merge_sort
result = merge_sort([3, 1, 2])
# Expected: [1, 2, 3]
# Got: ???
```

**Expected behavior:** What you expected.

**Actual behavior:** What actually happened.

**Failing test case:**
```python
assert merge_sort([3,1,2]) == [1,2,3]  # fails
```

**Environment:**
- Python version:
- OS:
