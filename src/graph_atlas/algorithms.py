from __future__ import annotations

from collections import deque
from typing import Deque, Dict, List, Optional, Set, Tuple, TypeVar

from .graph import Graph

T = TypeVar("T")


def bfs_tree(g: Graph[T], start: T) -> Tuple[List[T], Dict[T, Optional[T]]]:
    """
    BFS traversal from start.
    Returns (visit_order, parent_map) where parent_map[start] = None.
    """
    if start not in g:
        raise KeyError(f"Unknown start node: {start!r}")

    q: Deque[T] = deque([start])
    seen: Set[T] = {start}
    parent: Dict[T, Optional[T]] = {start: None}
    order: List[T] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(g.neighbors(u), key=repr):
            if v not in seen:
                seen.add(v)
                parent[v] = u
                q.append(v)

    return order, parent


def dfs_tree(g: Graph[T], start: T) -> Tuple[List[T], Dict[T, Optional[T]]]:
    """
    Iterative DFS traversal from start.
    Returns (visit_order, parent_map) where parent_map[start] = None.
    """
    if start not in g:
        raise KeyError(f"Unknown start node: {start!r}")

    stack: List[T] = [start]
    seen: Set[T] = set()
    parent: Dict[T, Optional[T]] = {start: None}
    order: List[T] = []

    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        order.append(u)

        # Reverse sorted push so traversal is stable-ish
        for v in sorted(g.neighbors(u), key=repr, reverse=True):
            if v not in seen:
                parent.setdefault(v, u)
                stack.append(v)

    return order, parent


def shortest_path_unweighted(g: Graph[T], src: T, dst: T) -> Optional[List[T]]:
    """
    Unweighted shortest path (BFS).
    Returns path [src, ..., dst] or None if unreachable.
    """
    if src not in g or dst not in g:
        raise KeyError("src and dst must be nodes in the graph")

    _, parent = bfs_tree(g, src)
    if dst not in parent:
        return None

    path: List[T] = []
    cur: Optional[T] = dst
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


def connected_components(g: Graph[T]) -> List[Set[T]]:
    """
    Connected components for UNDIRECTED graphs.
    (For directed graphs, this is not strongly connected components.)
    """
    if g.directed:
        raise ValueError("connected_components is for undirected graphs only")

    comps: List[Set[T]] = []
    remaining: Set[T] = set(g.nodes())

    while remaining:
        start = next(iter(remaining))
        order, _ = bfs_tree(g, start)
        comp = set(order)
        comps.append(comp)
        remaining -= comp

    return comps


def topo_sort(g: Graph[T]) -> List[T]:
    """
    Kahn's algorithm for topological sort.
    Directed graphs only. Raises ValueError if cyclic.
    """
    if not g.directed:
        raise ValueError("topo_sort requires a directed graph")

    nodes = g.nodes()
    indeg: Dict[T, int] = {n: 0 for n in nodes}

    for u in nodes:
        for v in g.neighbors(u):
            indeg[v] = indeg.get(v, 0) + 1

    q: Deque[T] = deque(sorted([n for n, d in indeg.items() if d == 0], key=repr))
    out: List[T] = []

    while q:
        u = q.popleft()
        out.append(u)
        for v in sorted(g.neighbors(u), key=repr):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(out) != len(indeg):
        raise ValueError("Graph contains a cycle; topological order does not exist")

    return out


def find_cycle(g: Graph[T]) -> Optional[List[T]]:
    """
    Directed cycle detection using DFS coloring.
    Returns a concrete cycle like ["a","b","c","a"] or None if acyclic.
    """
    if not g.directed:
        raise ValueError("find_cycle is for directed graphs only")

    WHITE, GRAY, BLACK = 0, 1, 2
    color: Dict[T, int] = {n: WHITE for n in g.nodes()}
    parent: Dict[T, Optional[T]] = {n: None for n in g.nodes()}

    def reconstruct(back_from: T, back_to: T) -> List[T]:
        # Build path back_from -> ... -> back_to and close loop
        path = [back_to]
        cur: Optional[T] = back_from
        while cur is not None and cur != back_to:
            path.append(cur)
            cur = parent[cur]
        path.append(back_to)
        path.reverse()
        return path

    def dfs(u: T) -> Optional[List[T]]:
        color[u] = GRAY
        for v in sorted(g.neighbors(u), key=repr):
            if color.get(v, WHITE) == WHITE:
                parent[v] = u
                cyc = dfs(v)
                if cyc is not None:
                    return cyc
            elif color[v] == GRAY:
                return reconstruct(u, v)
        color[u] = BLACK
        return None

    for n in sorted(g.nodes(), key=repr):
        if color[n] == WHITE:
            cyc = dfs(n)
            if cyc is not None:
                return cyc

    return None