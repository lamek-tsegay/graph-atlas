from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Generic, Iterable, List, Set, Tuple, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Edge(Generic[T]):
    """Edge record."""
    u: T
    v: T


class Graph(Generic[T]):
    """
    Adjacency-set graph with optional directed mode.

    Design goals:
    - readable API for real scripts/tools
    - correctness + clarity over micro-optimizations
    - avoids duplicate edges by using sets
    """

    def __init__(self, *, directed: bool = False) -> None:
        self.directed: bool = directed
        self._adj: Dict[T, Set[T]] = {}

    # --- mutation ---
    def add_node(self, node: T) -> None:
        """Add a node if it doesn't exist."""
        if node not in self._adj:
            self._adj[node] = set()

    def add_edge(self, u: T, v: T) -> None:
        """Add an edge u->v (and v->u if undirected). Auto-adds nodes."""
        self.add_node(u)
        self.add_node(v)
        self._adj[u].add(v)
        if not self.directed:
            self._adj[v].add(u)

    def remove_edge(self, u: T, v: T) -> None:
        """Remove an edge. No-op if missing."""
        if u in self._adj:
            self._adj[u].discard(v)
        if not self.directed and v in self._adj:
            self._adj[v].discard(u)

    def remove_node(self, node: T) -> None:
        """Remove a node and any incident edges. No-op if missing."""
        if node not in self._adj:
            return
        for n in list(self._adj.keys()):
            if n != node:
                self._adj[n].discard(node)
        del self._adj[node]

    # --- queries ---
    def nodes(self) -> List[T]:
        """Return nodes as a list (snapshot)."""
        return list(self._adj.keys())

    def neighbors(self, node: T) -> Set[T]:
        """Return a copy of the neighbors set."""
        if node not in self._adj:
            raise KeyError(f"Unknown node: {node!r}")
        return set(self._adj[node])

    def has_edge(self, u: T, v: T) -> bool:
        return u in self._adj and v in self._adj[u]

    def edges(self) -> List[Edge[T]]:
        """
        Return edges.
        For undirected graphs, returns each undirected edge once.
        """
        out: List[Edge[T]] = []
        if self.directed:
            for u, neigh in self._adj.items():
                for v in neigh:
                    out.append(Edge(u, v))
            return out

        seen: Set[Tuple[str, str]] = set()
        for u, neigh in self._adj.items():
            for v in neigh:
                a, b = (repr(u), repr(v))
                key = (a, b) if a <= b else (b, a)
                if key not in seen:
                    seen.add(key)
                    out.append(Edge(u, v))
        return out

    def __contains__(self, node: T) -> bool:
        return node in self._adj

    def __len__(self) -> int:
        return len(self._adj)

    def __repr__(self) -> str:
        kind = "directed" if self.directed else "undirected"
        return f"Graph({kind}, nodes={len(self._adj)}, edges={len(self.edges())})"