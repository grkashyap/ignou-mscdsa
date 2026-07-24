class TopologicalSort:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        """Add a directed edge from source to destination."""
        if not (0 <= source < self.num_vertices and
                0 <= destination < self.num_vertices):
            raise ValueError("Vertex is outside the graph")
        self.graph[source].append(destination)

    def sort(self):
        """Return a topological ordering using in-degrees."""
        in_degree = [0] * self.num_vertices

        # Count incoming edges for every vertex.
        for source in range(self.num_vertices):
            for destination in self.graph[source]:
                in_degree[destination] += 1

        # Start with vertices that have no incoming edges.
        queue = []
        for vertex in range(self.num_vertices):
            if in_degree[vertex] == 0:
                queue.append(vertex)

        topological_order = []

        while queue:
            current_vertex = queue.pop(0)
            topological_order.append(current_vertex)

            # Remove the outgoing edges of the selected vertex.
            for neighbour in self.graph[current_vertex]:
                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        if len(topological_order) != self.num_vertices:
            raise ValueError("Topological sort is not possible: graph has a cycle")

        return topological_order


if __name__ == "__main__":
    graph = TopologicalSort(6)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    order = graph.sort()
    print("Topological order:", " -> ".join(map(str, order)))
