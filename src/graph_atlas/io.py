from __future__ import annotations

from typing import Iterable, Tuple, TypeVar

from .graph import Graph

T = TypeVar("T")


def from_edge_list(edges: Iterable[Tuple[T, T]], *, directed: bool = False) -> Graph[T]:
    """Build a Graph from an iterable of (u, v) edges."""
    g: Graph[T] = Graph(directed=directed)
    for u, v in edges:
        g.add_edge(u, v)
    return g