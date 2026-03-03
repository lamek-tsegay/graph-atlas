# Architecture Overview

graph-atlas is structured as a minimal, modular graph toolkit.

## Core components

graph.py
- Defines Graph and Edge
- Stores adjacency sets
- Responsible only for structure management

algorithms.py
- Contains traversal and analysis algorithms
- Operates on Graph instances
- Does not modify graph structure

io.py
- Optional helper utilities
- Keeps parsing/loading separate from core logic

## Design Philosophy

- Minimal dependencies
- Clear separation of data structure and algorithms
- Readable implementations
- Developer-friendly return values