"""
graph-atlas: a lightweight graph toolkit for relationship networks.

Public API:
- Graph, Edge
- algorithms: bfs_tree, dfs_tree, shortest_path_unweighted, connected_components, topo_sort, find_cycle
- io: from_edge_list
"""

from .graph import Graph, Edge

__all__ = ["Graph", "Edge"]