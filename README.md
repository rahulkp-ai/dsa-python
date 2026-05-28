# 🧠 DSA-Python

<div align="center">
<br/>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Pytest-orange?style=for-the-badge&logo=pytest)](tests/)
[![Coverage](https://img.shields.io/badge/Coverage-85%25%2B-22c55e?style=for-the-badge)](tests/)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge)](https://github.com/psf/black)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](.github/workflows/)

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-rahulkp--ai-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahulkp-ai/)
[![GitHub](https://img.shields.io/badge/GitHub-rahulkp--ai-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rahulkp-ai)
[![Kaggle](https://img.shields.io/badge/Kaggle-rahulkpai-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/rahulkpai)

</div>

---

## 👤 Built by

```python
author = {
    "name"      : "RAHUL K P",
    "role"      : ["ML Engineer", "GenAI Engineer", "MSc CS Student @ 2026"],
    "location"  : "Kerala, India 🇮🇳",
    "certified" : "IBM Generative AI Engineering Professional",
    "why_dsa"   : "Strong algorithmic thinking = better ML systems 🧠",
    "contact"   : "rahulkpkurup@gmail.com"
}
```

> This repository is part of demonstrate **engineering discipline**, **clean code practices**, and **technical depth** as an ML Engineer.

---

## 🎯 What is DSA-Python?

A **production-quality** Data Structures & Algorithms repository in Python — combining the rigor of university coursework with the practicality of MAMAA interview prep.

Every module includes:

- ✅ **Type hints** — fully typed with `typing` module
- ✅ **Docstrings** — Google-style with examples
- ✅ **Big-O analysis** — time & space for every function
- ✅ **Unit tests** — pytest with >85% coverage
- ✅ **Jupyter notebooks** — theory + interactive code
- ✅ **CLI interface** — run algorithms from terminal
- ✅ **Benchmarks** — performance profiling with real data

---

## 📦 Topics Covered

| 📦 Category            | 🔢 Algorithms / Patterns                | 🧪 Tests | 📓 Notebook |
| ---------------------- | --------------------------------------- | -------- | ----------- |
| 🔢 Arrays              | 15+ patterns (prefix sum, kadane, etc.) | ✅       | ✅          |
| 🔤 Strings             | KMP, Rabin-Karp, Z-algorithm            | ✅       | ✅          |
| 🔗 Linked Lists        | Singly, Doubly, Cycle Detection         | ✅       | —           |
| 📚 Stacks & Queues     | Monotonic Stack, BFS Queue              | ✅       | —           |
| 🌲 Trees               | BT, BST, AVL, Traversals                | ✅       | ✅          |
| 🕸️ Graphs              | BFS, DFS, Dijkstra, Union-Find, MST     | ✅       | ✅          |
| 🧩 Dynamic Programming | 20+ problems (Knapsack, LCS, LIS)       | ✅       | ✅          |
| 🔀 Sorting             | 8 algorithms with complexity analysis   | ✅       | ✅          |
| 🔍 Searching           | Binary Search + 10 variants             | ✅       | —           |
| 🏔️ Heaps               | MinHeap, MaxHeap, Priority Queue        | ✅       | ✅          |
| 📖 Tries               | Prefix tree, Autocomplete               | ✅       | —           |
| ↩️ Backtracking        | N-Queens, Sudoku, Permutations          | ✅       | ✅          |
| 💡 Greedy              | Activity Selection, Huffman             | ✅       | —           |
| ⚡ Bit Manipulation    | XOR tricks, Bit DP                      | ✅       | ✅          |
| 👆 Two Pointers        | Merge, Palindrome, Container Water      | ✅       | ✅          |
| 🪟 Sliding Window      | Fixed + Variable window patterns        | ✅       | ✅          |
| 🔁 Recursion           | Factorial, Fibonacci, Tower of Hanoi    | ✅       | —           |
| 🗂️ Hashing             | Frequency maps, Anagrams, LRU           | ✅       | —           |
| ➗ Divide & Conquer    | Merge Sort, Quick Select, Closest Pair  | ✅       | —           |

---

## 🗺️ Learning Path

```
🌱 BEGINNER
├── Arrays & Strings      → Two Pointers, Prefix Sum, Sliding Window
├── Basic Sorting         → Bubble, Insertion, Selection
└── Recursion Basics      → Factorial, Fibonacci, Towers of Hanoi

🌿 INTERMEDIATE
├── Linked Lists          → Singly, Doubly, Cycle Detection
├── Stacks & Queues       → Monotonic Stack, BFS
├── Trees & BST           → Traversals, Height, LCA
├── Hash Maps             → Frequency counting, Anagrams
└── Binary Search         → Rotated arrays, Search on answer

🌳 ADVANCED
├── Graphs                → BFS/DFS, Dijkstra, Union-Find, MST
├── Dynamic Programming   → Knapsack, LCS, LIS, Edit Distance
├── Heaps                 → Priority Queue, Median Finder
├── Tries                 → Prefix matching, Autocomplete
├── Backtracking          → N-Queens, Sudoku, Permutations
└── Greedy                → Activity Selection, Huffman Coding

🏆 EXPERT
├── Advanced Graphs       → Bellman-Ford, Floyd-Warshall, Topological Sort
├── Divide & Conquer      → Closest Pair, Strassen, FFT intro
├── Bit Manipulation      → XOR tricks, Bit DP
└── Competitive Patterns  → Mo's Algorithm, Segment Trees
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/rahulkp-ai/dsa-python.git
cd dsa-python

# 2. Auto setup (recommended)
chmod +x setup.sh && ./setup.sh
source venv/bin/activate

# 3. Or manual install
pip install -r requirements.txt
pip install -e .

# 4. Run all tests
make test

# 5. Run benchmarks
make benchmark

# 6. Launch Jupyter notebooks
make notebooks

# 7. Try the CLI
dsa --help
```

---

## 📁 Repository Structure

```
dsa-python/
├── src/                          # ⚙️  All algorithm implementations
│   ├── arrays/                   #     Array algorithms & patterns
│   ├── strings/                  #     String algorithms
│   ├── linked_list/              #     Singly, Doubly, Cycle Detection
│   ├── stacks_queues/            #     Stack, Queue, Monotonic Stack
│   ├── trees/                    #     Binary Tree, BST, AVL
│   ├── graphs/                   #     BFS/DFS, Dijkstra, MST
│   ├── dynamic_programming/      #     DP patterns & solutions
│   ├── sorting/                  #     8 sorting algorithms
│   ├── searching/                #     Binary search variants
│   ├── heaps/                    #     MinHeap, MaxHeap
│   ├── tries/                    #     Trie data structure
│   ├── backtracking/             #     Backtracking problems
│   ├── greedy/                   #     Greedy algorithms
│   ├── bit_manipulation/         #     Bit tricks
│   ├── two_pointers/             #     Two pointer patterns
│   ├── sliding_window/           #     Sliding window patterns
│   ├── recursion/                #     Recursive patterns
│   ├── hashing/                  #     Hash-based solutions
│   ├── divide_conquer/           #     Divide & conquer
│   ├── math_algorithms/          #     GCD, Primes, Modular Arith.
│   ├── cli/                      #     Typer CLI app
│   └── dashboard/                #     Rich terminal dashboard
│
├── notebooks/                    # 📓  Jupyter notebooks (theory + code)
│   ├── 01_sorting_algorithms.ipynb
│   ├── 02_dynamic_programming.ipynb
│   ├── 03_graph_algorithms.ipynb
│   ├── 04_trees_and_bst.ipynb
│   ├── 05_heaps_priority_queues.ipynb
│   ├── 06_backtracking.ipynb
│   ├── 07_string_algorithms.ipynb
│   ├── 08_two_pointers_sliding_window.ipynb
│   ├── 09_bit_manipulation.ipynb
│   └── 10_complexity_reference.ipynb
│
├── tests/                        # 🧪  Full test suite
│   ├── unit/                     #     Unit tests per module (17 files)
│   ├── integration/              #     Cross-module integration tests
│   └── stress/                   #     Large-input stress tests
│
├── benchmarks/                   # 📊  Performance benchmarking
├── interview_prep/               # 💼  FAANG interview guides
│   ├── faang_patterns.md         #     14 core patterns
│   ├── top_150_problems.md       #     Top 150 LeetCode problems
│   └── roadmap_3months.md        #     3-month study roadmap
│
├── resources/                    # 📚  Cheat sheets & references
│   ├── complexity_cheatsheet.md  #     Big-O for all structures
│   ├── python_tricks.md          #     Python DSA tips
│   ├── dsa_roadmap.md            #     Full DSA roadmap
│   └── competitive_programming.md
│
├── problems/                     # 🧩  Curated problems by difficulty
│   ├── easy/
│   ├── medium/
│   └── hard/
│
├── solutions/                    # ✅  Optimized solutions with analysis
├── datasets/                     # 🗃️  Test data generators
├── docs/                         # 📖  Extended documentation
├── .github/                      # 🤖  CI/CD workflows + templates
│   └── workflows/                #     pytest, lint, format, notebook CI
├── pyproject.toml                # 📦  Project config (Black, MyPy, isort)
├── Makefile                      # ⚡  make test / benchmark / format
└── requirements.txt
```

---

## 📊 Complexity Quick Reference

| Algorithm     | Best       | Average    | Worst      | Space    |
| ------------- | ---------- | ---------- | ---------- | -------- |
| Bubble Sort   | O(n)       | O(n²)      | O(n²)      | O(1)     |
| Merge Sort    | O(n log n) | O(n log n) | O(n log n) | O(n)     |
| Quick Sort    | O(n log n) | O(n log n) | O(n²)      | O(log n) |
| Heap Sort     | O(n log n) | O(n log n) | O(n log n) | O(1)     |
| Binary Search | O(1)       | O(log n)   | O(log n)   | O(1)     |
| BFS / DFS     | O(V+E)     | O(V+E)     | O(V+E)     | O(V)     |
| Dijkstra      | O(E)       | O(E log V) | O(E log V) | O(V)     |
| Knapsack DP   | O(nW)      | O(nW)      | O(nW)      | O(W)     |

---

## 💼 Interview Preparation

| Resource                                                                   | Description                                 |
| -------------------------------------------------------------------------- | ------------------------------------------- |
| [`interview_prep/faang_patterns.md`](interview_prep/faang_patterns.md)     | 14 core FAANG patterns with templates       |
| [`interview_prep/top_150_problems.md`](interview_prep/top_150_problems.md) | Top 150 LeetCode problems mapped to modules |
| [`interview_prep/roadmap_3months.md`](interview_prep/roadmap_3months.md)   | Structured 3-month study plan               |
| [`resources/complexity_cheatsheet.md`](resources/complexity_cheatsheet.md) | Big-O cheat sheet for all data structures   |
| [`resources/python_tricks.md`](resources/python_tricks.md)                 | Python-specific DSA tips & patterns         |

---

## 🧪 Running Tests

```bash
# All tests
make test

# Unit tests only
pytest tests/unit/ -v

# With coverage report
pytest --cov=src --cov-report=html

# Stress tests
pytest tests/stress/ -v
```

---

## 🤝 Contributing

This is an open learning project. Contributions are welcome!

```bash
# Fork & clone
git checkout -b feature/your-algorithm

# Code, format, lint, test
make format && make lint && make test

# Submit PR
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## 📜 License

MIT License — see [LICENSE](LICENSE).

---

<div align="center">

<br/>

**Built by [RAHUL K P](https://github.com/rahulkp-ai) — ML Engineer · GenAI · MSc CS @ 2026**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-rahulkp--ai-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahulkp-ai/)
[![Kaggle](https://img.shields.io/badge/Kaggle-rahulkpai-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/rahulkpai)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--3403--6670-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0009-3403-6670)

<br/>

_⭐ Star this repo if it helped your prep — and connect on LinkedIn!_

</div>
