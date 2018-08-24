# Uses python3

import sys
import logging
logging.basicConfig(level=logging.DEBUG, filename='debug.log')


class Node:
    def __init__(self, node_num):
        self.num = node_num
        self.connections = dict()
        self.dist_from_self = dict()

    def add_connection(self, node, distance):
        self.connections[node] = distance
        self.dist_from_self[node] = distance

    def update_dist_from_self(self, source_node):
        dist_from_source = self.dist_from_self[source_node]
        for node, edge_dist in source_node.connections.items():
            dist_to_node = dist_from_source+edge_dist
            if (self.dist_from_self[node] is None or
                    self.dist_from_self[node] > dist_to_node):
                self.dist_from_self[node] = dist_to_node

    def __repr__(self):
        return 'Node({})'.format(self.num)


def negative_cycle(nodes):
    for source in nodes:
        continue


def build_graph(num_nodes, edges):
    nodes = [Node(i) for i in range(num_nodes)]
    if len(edges) > 0:
        for source_node_ind, dest_node_ind, weight in edges:
            logging.debug(f'{source_node_ind}:{dest_node_ind}:{weight}')
            s = source_node_ind - 1
            d = dest_node_ind - 1
            nodes[s].connections[nodes[d]] = weight

    return nodes


def parse_input(data):

    num_nodes, _ = data[:2]
    edges = list(
        zip(data[2::3], data[3::3], data[4::3]))
    return num_nodes, edges


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    num_nodes, edges = parse_input(data)
    nodes = build_graph(num_nodes, edges)

    print(negative_cycle(nodes))
