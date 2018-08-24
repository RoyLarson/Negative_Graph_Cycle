import negative_cycle as nc


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
    node = nc.Node(0)
    assert type(node) == nc.Node
    assert node.num == 0

    node_2 = nc.Node(1)
    node.add_connection(node_2, 1)
    assert node_2 in node.connections
    node_2.update_dist_from_source(node, node.connections[node_2])
    assert node in node_2._dist_from_source
    assert node_2.get_dist_from_source(node) == 1


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
