from queue import Queue
from graph import generate_cubic_graph
from timeit import default_timer as timer


def bfs(graph: dict, start_node: tuple) -> list:
    """
    Perform a breadth-first search on the graph starting from the start node.
    Returns a list of nodes in the order they were visited.
    """
    visited = set()
    queue = Queue()
    queue.put(start_node)
    visited.add(start_node)

    order_of_visit = []

    while not queue.empty():
        node = queue.get()
        order_of_visit.append(node)

        if node in graph.keys():
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.put(neighbor)

    return order_of_visit


if __name__ == "__main__":
    t = 0
    n = 5

    for _ in range(n):
        cubic_graph = generate_cubic_graph(500)
        start = timer()
        bfs_result = bfs(cubic_graph, (0, 0, 0))
        end = timer()
        t += end - start

    print(f"Average running time of sequential algorithm: {t / n} sec.")
