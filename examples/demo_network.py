from graph_atlas.graph import Graph
from graph_atlas.algorithms import (
    bfs_tree,
    shortest_path_unweighted,
    connected_components,
    find_cycle,
)


def main() -> None:
    # Undirected relationship graph (social/collaboration network)
    network = Graph(directed=False)

    network.add_edge("alice", "bob")
    network.add_edge("alice", "carol")
    network.add_edge("bob", "dave")
    network.add_edge("eve", "frank")

    print("Graph:", network)

    order, _ = bfs_tree(network, "alice")
    print("Reachable from alice:", order)

    path = shortest_path_unweighted(network, "alice", "dave")
    print("Connection path alice -> dave:", path)

    comps = connected_components(network)
    print("Communities:", comps)

    # Directed influence/dependency graph (cycle example)
    influence = Graph(directed=True)
    influence.add_edge("auth", "billing")
    influence.add_edge("billing", "search")
    influence.add_edge("search", "auth")  # cycle

    cycle = find_cycle(influence)
    print("Cycle detected:", cycle)


if __name__ == "__main__":
    main()