"""Edmonds-Karp maximum flow and minimum-cut certificate.

This is a graph algorithm for abstract directed capacitated networks.
It is not an electrical power-flow solver.
"""
from collections import deque


def maximum_flow(nodes, edges, source, sink):
    """Return (max_flow, source_side, edge_flows, cut_edges).

    nodes: iterable of unique node labels
    edges: iterable of (tail, head, nonnegative_capacity)
    Parallel directed arcs are supported. Self-loops are rejected.
    """
    node_list = list(nodes)
    if len(set(node_list)) != len(node_list):
        raise ValueError("node labels must be unique")
    node_set = set(node_list)
    if source not in node_set or sink not in node_set:
        raise ValueError("source and sink must be in nodes")
    if source == sink:
        raise ValueError("source and sink must differ")

    adjacency = {node: [] for node in node_list}
    originals = []
    for tail, head, capacity in edges:
        if tail not in node_set or head not in node_set:
            raise ValueError("edge endpoint is not in nodes")
        if tail == head:
            raise ValueError("self-loops are not supported")
        if not isinstance(capacity, (int, float)) or capacity < 0:
            raise ValueError("capacities must be nonnegative numbers")
        forward_index = len(adjacency[tail])
        reverse_index = len(adjacency[head])
        adjacency[tail].append([head, reverse_index, float(capacity)])
        adjacency[head].append([tail, forward_index, 0.0])
        originals.append((tail, forward_index, head, float(capacity)))

    total_flow = 0.0
    while True:
        parent = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            node = queue.popleft()
            for edge_index, edge in enumerate(adjacency[node]):
                neighbor, _, residual = edge
                if residual > 1e-12 and neighbor not in parent:
                    parent[neighbor] = (node, edge_index)
                    queue.append(neighbor)
                    if neighbor == sink:
                        break
        if sink not in parent:
            break

        increment = float("inf")
        node = sink
        while node != source:
            previous, edge_index = parent[node]
            increment = min(increment, adjacency[previous][edge_index][2])
            node = previous

        node = sink
        while node != source:
            previous, edge_index = parent[node]
            edge = adjacency[previous][edge_index]
            reverse_node, reverse_index = edge[0], edge[1]
            edge[2] -= increment
            adjacency[reverse_node][reverse_index][2] += increment
            node = previous
        total_flow += increment

    source_side = set()
    queue = deque([source])
    source_side.add(source)
    while queue:
        node = queue.popleft()
        for neighbor, _, residual in adjacency[node]:
            if residual > 1e-12 and neighbor not in source_side:
                source_side.add(neighbor)
                queue.append(neighbor)

    edge_flows = []
    cut_edges = []
    for tail, index, head, capacity in originals:
        residual = adjacency[tail][index][2]
        flow = capacity - residual
        edge_flows.append((tail, head, flow))
        if tail in source_side and head not in source_side:
            cut_edges.append((tail, head, capacity))

    return total_flow, source_side, edge_flows, cut_edges


def case_study():
    nodes = ("s", "a", "b", "t")
    edges = (
        ("s", "a", 7),
        ("s", "b", 5),
        ("a", "b", 2),
        ("a", "t", 4),
        ("b", "t", 8),
    )
    return maximum_flow(nodes, edges, "s", "t")


if __name__ == "__main__":
    value, source_side, flows, cut = case_study()
    print(f"Maximum flow: {value:.1f} MW")
    print("Arc flows:")
    for tail, head, flow in flows:
        print(f"  {tail} -> {head}: {flow:.1f} MW")
    print(f"Minimum-cut source side: {sorted(source_side)}")
    print(f"Cut capacity: {sum(edge[2] for edge in cut):.1f} MW")
