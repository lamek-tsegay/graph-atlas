# graph-atlas

A lightweight graph toolkit for modeling and analyzing **relationship networks** — social graphs, knowledge graphs, service maps, and dependency graphs.

This project is intentionally small but structured like a real package:
- Clean, importable API
- Core graph algorithms
- Unit tests
- Runnable examples
- Proper `src/` layout

---

## Why this exists

Graphs power many real-world systems:

- Social networks (reachability, shortest connection paths)
- Knowledge graphs (entity exploration)
- Service dependency maps (cycle detection, impact analysis)
- Build pipelines and workflows (topological ordering)

`graph-atlas` focuses on clarity, correctness, and developer experience.

---

## Features

### Graph data structure
- Directed or undirected graphs
- Adjacency-set representation (no duplicate edges)
- Add/remove nodes and edges
- Query neighbors and edges

### Algorithms
- BFS traversal (returns visit order + parent tree)
- DFS traversal (iterative)
- Unweighted shortest path (BFS)
- Connected components (undirected graphs)
- Topological sort (directed acyclic graphs)
- Directed cycle detection

### Developer workflow
- Unit tests with `pytest`
- Runnable example scripts in `examples/`
- Clean `src/` package layout

---

## Project layout

```
graph-atlas/
├── src/
│   └── graph_atlas/
│       ├── __init__.py
│       ├── graph.py
│       ├── algorithms.py
│       └── io.py
├── tests/
├── examples/
│   └── demo_network.py
├── pyproject.toml
└── README.md
```

---

## Installation

Create a virtual environment and install in editable mode:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest
```

---

## Quick start

### Social network example

```python
from graph_atlas.graph import Graph
from graph_atlas.algorithms import shortest_path_unweighted, connected_components

g = Graph(directed=False)
g.add_edge("alice", "bob")
g.add_edge("bob", "carol")
g.add_edge("dave", "eve")

print(shortest_path_unweighted(g, "alice", "carol"))
print(connected_components(g))
```

### Dependency graph example

```python
from graph_atlas.graph import Graph
from graph_atlas.algorithms import topo_sort, find_cycle

deps = Graph(directed=True)
deps.add_edge("build", "test")
deps.add_edge("test", "package")

print(find_cycle(deps))   # None if acyclic
print(topo_sort(deps))    # Valid order if DAG
```

---

## Running the demo

```bash
PYTHONPATH=src python3 examples/demo_network.py
```

---

## Running tests

```bash
pytest -q
```

---

## Design notes

### Representation

The graph uses adjacency sets:

```
adj[node] = set(neighbors)
```

Benefits:
- Fast neighbor lookup
- No duplicate edges
- Clean algorithm implementations

### Return values

Algorithms return developer-friendly structures:
- Traversal order + parent map
- Explicit path lists
- Topological ordering as a list
- Concrete cycles like `["auth", "billing", "search", "auth"]`

---

## Possible extensions

- Weighted shortest path (Dijkstra)
- Strongly connected components
- Graphviz export (DOT format)
- Performance benchmarking
- CLI interface

---

## Academic integrity note

This repository is a portfolio-oriented implementation with original structure and examples. It is not intended for coursework submission or reuse.

---

## License

MIT