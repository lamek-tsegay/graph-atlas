from graph_atlas.graph import Graph
from graph_atlas.algorithms import bfs_tree, dfs_tree, shortest_path_unweighted


def test_bfs_parent_and_order_basic():
    g = Graph(directed=False)
    g.add_edge("alice", "bob")
    g.add_edge("alice", "carol")
    g.add_edge("bob", "dave")

    order, parent = bfs_tree(g, "alice")
    assert order[0] == "alice"
    assert parent["alice"] is None
    assert parent["bob"] == "alice"
    assert parent["carol"] == "alice"
    assert parent["dave"] == "bob"


def test_dfs_visits_all_reachable():
    g = Graph(directed=False)
    g.add_edge("u1", "u2")
    g.add_edge("u2", "u3")
    g.add_edge("u2", "u4")

    order, parent = dfs_tree(g, "u1")
    assert set(order) == {"u1", "u2", "u3", "u4"}
    assert parent["u1"] is None


def test_shortest_path_unweighted():
    g = Graph(directed=True)
    g.add_edge("onboarding", "profile")
    g.add_edge("profile", "recommendations")
    g.add_edge("onboarding", "feed")
    g.add_edge("feed", "recommendations")

    path = shortest_path_unweighted(g, "onboarding", "recommendations")
    assert path in (
        ["onboarding", "profile", "recommendations"],
        ["onboarding", "feed", "recommendations"],
    )