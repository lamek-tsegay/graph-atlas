import pytest

from graph_atlas.graph import Graph
from graph_atlas.algorithms import find_cycle, topo_sort


def test_cycle_detection_none_when_acyclic():
    deps = Graph(directed=True)
    deps.add_edge("build", "test")
    deps.add_edge("test", "package")

    assert find_cycle(deps) is None
    assert topo_sort(deps) == ["build", "test", "package"]


def test_cycle_detection_finds_cycle():
    g = Graph(directed=True)
    g.add_edge("auth", "billing")
    g.add_edge("billing", "search")
    g.add_edge("search", "auth")  # cycle

    cyc = find_cycle(g)
    assert cyc is not None
    assert cyc[0] == cyc[-1]

    with pytest.raises(ValueError):
        topo_sort(g)