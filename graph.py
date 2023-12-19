def generate_cubic_graph(x: int) -> dict:
    """
    Generate a cubic graph represented as a dictionary.
    Each node is a tuple (x, y, z), and its value is a list of neighboring nodes.
    """
    graph = {}
    for x in range(x):
        for y in range(x):
            for z in range(x):
                # Define neighbors (consider edge cases)
                neighbors = []
                if x > 0:
                    neighbors.append((x-1, y, z))
                if x < x-1:
                    neighbors.append((x+1, y, z))
                if y > 0:
                    neighbors.append((x, y-1, z))
                if y < x-1:
                    neighbors.append((x, y+1, z))
                if z > 0:
                    neighbors.append((x, y, z-1))
                if z < x-1:
                    neighbors.append((x, y, z+1))

                graph[(x, y, z)] = neighbors

    return graph
