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
    assert nodes[0].dist_from_self[nodes[1]] == edge_weights[0]
    assert nodes[2] not in nodes[0].connections
    assert nodes[1].dist_from_self[nodes[2]] == edge_weights[1]


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

    assert nc.negative_cycle(nodes) == 1

    negative_test = [4, 4, 1, 2, 5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    num_nodes, edges = nc.parse_input(negative_test)
    nodes = nc.build_graph(num_nodes, edges)

    assert nc.negative_cycle(nodes) == 0


if __name__ == '__main__':
    test_parse_input()
    test_node()
    test_build_graph()
    test_negative_cycle()
