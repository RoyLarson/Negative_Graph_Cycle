# Uses python3

import sys
import logging
logging.basicConfig(level=logging.DEBUG, filename='debug.log')


class Node:
    def __init__(self, node_num):
        self.num = node_num
        self.connections = dict()
        self.dist_from_self = dict()
        self.updated = False

    def add_connection(self, node, distance):
        self.connections[node] = distance

    def update_dist_from_self(self, current_node):
        self.updated = False
        current_dist_from_self = self.dist_from_self[current_node]
        for node, edge_dist in current_node.connections.items():
            dist_to_node = current_dist_from_self+edge_dist
            try:
                self.dist_from_self[node]
            except KeyError:
                self.dist_from_self[node] = dist_to_node
                self.updated = True
            else:
                if dist_to_node < self.dist_from_self[node]:
                    self.dist_from_self[node] = dist_to_node
                    self.updated = True

    def __repr__(self):
        return 'Node({})'.format(self.num)


def negative_cycle(nodes):
    nlist = nodes[:]
    nodeset = set(nodes)
    searched = set()
    while len(searched) < len(nodes):
        not_searched = list(nodeset.difference(searched))
        source = not_searched[0]
        for i in range(len(nlist)):
            an_update = False
            visited = set()
            queue = [source]
            q_index = 0
            while q_index < len(queue):
                current_node = queue[q_index]
                if current_node in visited:
                    q_index += 1
                    continue
                else:
                    source.update_dist_from_self(current_node)
                    visited.add(current_node)
                    if source.updated:
                        an_update = True
                        searched.add(current_node)
                    queue.append(*current_node.connections)
                    q_index += 1
            if not an_update:
                break

    return source.updated


def build_graph(num_nodes, edges):
    nodes = [Node(i) for i in range(num_nodes)]
    for node in nodes:
        node.dist_from_self[node] = 0

    if len(edges) > 0:
        for source_node_ind, dest_node_ind, weight in edges:
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
