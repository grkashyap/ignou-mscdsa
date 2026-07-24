class DijkstraAlgorithm:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def dijkstra(self, source):
        """Return shortest distances and predecessors from *source*.

        A zero weight in the adjacency matrix denotes that no edge exists.
        """
        if not 0 <= source < self.num_vertices:
            raise ValueError("Source vertex is outside the graph")

        visited = set()
        distance_from_source = [float("inf")] * self.num_vertices
        previous = [None] * self.num_vertices
        distance_from_source[source] = 0

        for _ in range(self.num_vertices):
            current_node = None
            minimum_distance = float("inf")

            for vertex in range(self.num_vertices):
                if (vertex not in visited and
                        distance_from_source[vertex] < minimum_distance):
                    current_node = vertex
                    minimum_distance = distance_from_source[vertex]

            # Remaining vertices are unreachable from the source.
            if current_node is None:
                break

            visited.add(current_node)

            for neighbour, edge_weight in enumerate(self.graph[current_node]):
                if edge_weight > 0 and neighbour not in visited:
                    new_distance = (distance_from_source[current_node] +
                                    edge_weight)
                    if new_distance < distance_from_source[neighbour]:
                        distance_from_source[neighbour] = new_distance
                        previous[neighbour] = current_node

        return distance_from_source, previous

    def get_path(self, prev, source, target):
        """Return the path from *source* to *target*, or an empty list."""
        path = []

        while target is not None:
            path.append(target)
            target = prev[target]

        path.reverse()
        return path if path[0] == source else []

if __name__ == '__main__':
    input_num_vertices = 4
    alg = DijkstraAlgorithm(input_num_vertices)
    alg.graph = [
        [0, 2, 6, 0],
        [2, 0, 9, 5],
        [6, 9, 0, 8],
        [0, 5, 8, 0]
    ]
    start = 0
    end = 3
    distances, prev_lst = alg.dijkstra(start)
    g_path = alg.get_path(prev_lst, start, end)

    print("Shortest distances from vertex 0:", distances)
    print("Shortest path from vertex 0 to vertex 3:", " -> ".join(map(str, g_path)))
