import negative_cycle as nc
from random import randrange


def test_parse_input():
    normal = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    num_nodes, edges = nc.parse_input(normal)
    correct_edges = [(1, 2, -5), (4, 1, 2), (2, 3, 2), (3, 1, 1)]
    assert num_nodes == 4
    assert edges == correct_edges

    no_edges = [5, 0]
    num_nodes, edges = nc.parse_input(no_edges)
    correct_edges = []
    assert num_nodes == 5
    assert edges == correct_edges


def test_node():
    node_0 = nc.Node(0)
    assert type(node_0) == nc.Node
    assert node_0.num == 0

    nodes = [node_0]
    for i in range(1, 5):
        nodes.append(nc.Node(i))

    edge_weights = []
    for i in range(4):
        edge_weights.append(randrange(1, 10))

    for i in range(4):
        nodes[i].add_connection(nodes[i+1], edge_weights[i])

    assert nodes[1] in nodes[0].connections
    assert nodes[2] not in nodes[0].connections


def test_build_graph():
    normal = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    num_nodes, edges = nc.parse_input(normal)
    nodes = nc.build_graph(num_nodes, edges)
    assert len(nodes) == 4

    for source_node_ind, end_node_ind, edge_weight in edges:
        source_node = nodes[source_node_ind - 1]
        end_node = nodes[end_node_ind-1]
        assert end_node in source_node.connections
        assert source_node.connections[end_node] == edge_weight

    no_edges = [5, 0]
    num_nodes, edges = nc.parse_input(no_edges)
    nodes = nc.build_graph(num_nodes, edges)


def test_negative_cycle():
    positive_test = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    num_nodes, edges = nc.parse_input(positive_test)
    nodes = nc.build_graph(num_nodes, edges)

    assert nc.negative_cycle(nodes)


def test_negative_cycle_2():
    negative_test = [4, 4, 1, 2, 5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    num_nodes, edges = nc.parse_input(negative_test)
    nodes = nc.build_graph(num_nodes, edges)

    assert not nc.negative_cycle(nodes)


def test_negative_cycle_3():
    negative_test = [10, 9, 1, 2, 1, 5, 6, 1, 6, 7, 1, 8, 9, 1,
                     9, 10, 1, 3, 4, 1, 7, 8, 1, 4, 5, 1, 2, 3, 1, ]

    num_nodes, edges = nc.parse_input(negative_test)
    nodes = nc.build_graph(num_nodes, edges)

    assert not nc.negative_cycle(nodes)


def test_negative_cycle_unconnected():
    """
    unconnected graph
    """
    test = [10, 0]
    num_nodes, edges = nc.parse_input(test)
    nodes = nc.build_graph(num_nodes, edges)

    assert not nc.negative_cycle(nodes)


def test_isolated_not_negative_cycle():
    test = [10, 8,
            1, 2, 1,
            2, 3, 1,
            3, 4, 1,
            5, 6, 1,
            6, 1, 1,
            7, 8, 1,
            8, 9, 1,
            9, 7, 1]

    num_nodes, edges = nc.parse_input(test)
    nodes = nc.build_graph(num_nodes, edges)

    assert not nc.negative_cycle(nodes)


def test_isolated_negative_cycle():
    test = [10, 8,
            1, 2, 1,
            2, 3, 1,
            3, 4, 1,
            5, 6, 1,
            6, 1, 1,
            7, 8, 1,
            8, 9, -5,
            9, 7, 1]

    num_nodes, edges = nc.parse_input(test)
    nodes = nc.build_graph(num_nodes, edges)

    assert nc.negative_cycle(nodes)


def test_fully_connected_graph_w_negative_cycle():
    test = [6, 30,
            1, 2, 1,
            1, 3, 1,
            1, 4, 1,
            1, 5, 1,
            1, 6, 1,
            2, 1, -2,
            2, 3, 1,
            2, 4, 1,
            2, 5, 1,
            2, 6, 1,
            3, 1, -1,
            3, 2, 1,
            3, 4, 1,
            3, 5, 1,
            3, 6, 1,
            4, 1, -5,
            4, 2, 5,
            4, 3, 1,
            4, 5, 1,
            4, 6, 1,
            5, 1, 1,
            5, 2, -5,
            5, 3, 1,
            5, 4, 1,
            5, 6, 1,
            6, 1, 1,
            6, 2, 1,
            6, 3, 1,
            6, 4, 1,
            6, 5, 1]

    num_nodes, edges = nc.parse_input(test)
    nodes = nc.build_graph(num_nodes, edges)

    assert nc.negative_cycle(nodes)


if __name__ == '__main__':
    #    test_parse_input()
    #    test_node()
    #    test_build_graph()
    #    test_negative_cycle()
    #    test_negative_cycle_3()
    test_fully_connected_graph_w_negative_cycle()
