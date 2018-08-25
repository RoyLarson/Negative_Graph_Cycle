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
        try:
            dist_from_source = self.dist_from_self[current_node]
        except KeyError:
            return
        else:
            for node, edge_dist in current_node.connections.items():
                dist_to_node = dist_from_source+edge_dist
                if (self.dist_from_self[node] is None or
                        self.dist_from_self[node] > dist_to_node):
                    self.dist_from_self[node] = dist_to_node
                    self.updated = True

    def __repr__(self):
        return 'Node({})'.format(self.num)


def negative_cycle(nodes):
    raise Exception
    nlist = nodes[:]
    searched = set()
    source_index = len(nlist)-1
    while len(searched) < len(nodes):
        source = nlist[source_index]
        searched.add(source)
        for i in range(len(nlist)+1):
            visited = set()
            queue = []
            queue.append(*source.connections)
            q_index = 0
            while q_index < len(queue):
                if queue[q_index] in visited:
                    q_index += 1
                    continue
                else:
                    source.update_dist_from_self(queue[q_index])
                    visited.add(queue[q_index])
                    if source.updated:

                        searched.add(queue[q_index])
                    queue.append(*queue[q_index].connections)
                    q_index += 1

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
