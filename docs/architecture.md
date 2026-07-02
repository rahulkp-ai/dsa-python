# Repository Architecture

## Overview

```
DSA-Python/
├── src/                    # Core implementations (18 modules)
├── tests/                  # Pytest suite (unit + integration + stress)
├── benchmarks/             # Performance profiling scripts
├── notebooks/              # Jupyter educational notebooks
├── interview_prep/         # FAANG interview guides
├── resources/              # Cheat sheets, roadmaps
├── problems/               # Curated problems by difficulty
├── solutions/              # Optimized solutions
├── datasets/               # Test data generators
├── docs/                   # Extended documentation
├── src/cli/                # Command-line interface
└── src/dashboard/          # Streamlit dashboard
```

## Design Principles

1. **Single Responsibility** — Each file covers exactly one topic
2. **Educational First** — Code is written to teach, not just solve
3. **Production Quality** — Type hints, docstrings, PEP8, tests
4. **Progressive Complexity** — Easy → Medium → Hard within each module
5. **Self-Documenting** — Docstrings include time/space complexity

## Module Dependencies

```
src/sorting         → no internal deps
src/searching       → no internal deps
src/arrays          → no internal deps
src/strings         → no internal deps
src/bit_manipulation→ no internal deps
src/math_algorithms → no internal deps
src/recursion       → no internal deps
src/two_pointers    → no internal deps
src/sliding_window  → no internal deps
src/stacks_queues   → no internal deps
src/hashing         → no internal deps
src/linked_list     → no internal deps
src/trees           → no internal deps
src/heaps           → no internal deps
src/tries           → no internal deps
src/graphs          → no internal deps (uses heapq)
src/dynamic_programming → no internal deps
src/backtracking    → no internal deps
src/greedy          → no internal deps
src/cli/main        → imports from all src modules
src/dashboard/app   → imports from all src modules
```

## Adding a New Algorithm

1. Identify the correct module in `src/`
2. Follow the template:

```python
def algorithm_name(input: List[int]) -> int:
    """
    One-line summary.

    Detailed explanation.
    Time Complexity: O(...)
    Space Complexity: O(...)

    Args:
        input: Description.
    Returns:
        Description.
    Examples:
        >>> algorithm_name([1,2,3])
        6
    """
    # Implementation
    pass
```

3. Add `if __name__ == "__main__"` demo
4. Add unit tests in `tests/unit/test_<module>.py`
5. Run `make format && make lint && make test`
