# Datasets

Test data generators and sample datasets for benchmarking and testing.

## Files

| File | Description |
|------|-------------|
| `generate.py` | Generate random test arrays and graphs |
| `sample_graphs.py` | Pre-built graph examples |
| `test_arrays.py` | Common test case arrays |

## Usage

```python
from datasets.generate import random_array, random_graph, nearly_sorted

arr = random_array(1000)
graph = random_graph(50, edge_prob=0.3)
```
