from multiprocessing import Pool
from bfs import bfs
from graph import generate_cubic_graph
from timeit import default_timer as timer


def par_bfs_worker(args: tuple) -> list:
    """
    Worker function for parallel BFS.
    Takes a tuple of (graph, start node) and performs BFS from that start node.
    """
    graph, start_node = args
    return bfs(graph, start_node)


def par_bfs(graph: dict, start_nodes: list, pool_size: int) -> list:
    """
    Perform a parallel BFS on the graph.
    The graph is divided among different start nodes.
    """
    # Create a pool of workers
    with Pool(pool_size) as pool:
        # Map the graph and start nodes to the worker function
        results = pool.map(
            par_bfs_worker,
            [(graph, start_node) for start_node in start_nodes]
        )

    # Combine results from all workers
    combined_result = []
    for result in results:
        combined_result.extend(result)

    return combined_result


if __name__ == "__main__":
    t = 0
    n = 1

    for _ in range(n):
        cubic_graph = generate_cubic_graph(500)
        start = timer()
        par_bfs_result = par_bfs(
            cubic_graph,
            [(0, 0, 0), (1, 1, 1), (3, 3, 3), (4, 4, 4)],
            4
        )
        end = timer()
        t += end - start

    print(f"Average running time of parallel algorithm: {t / n} sec.")
