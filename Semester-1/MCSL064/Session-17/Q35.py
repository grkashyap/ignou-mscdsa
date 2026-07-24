class KruskalAlgorithm:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        """Add an undirected weighted edge to the graph."""
        if not (0 <= source < self.num_vertices and
                0 <= destination < self.num_vertices):
            raise ValueError("Vertex is outside the graph")
        self.edges.append((weight, source, destination))

    def kruskal(self):
        """Return the minimum spanning tree edges and their total cost."""
        parent = list(range(self.num_vertices))
        minimum_spanning_tree = []
        minimum_cost = 0

        # Process edges from the smallest weight to the largest weight.
        for weight, source, destination in sorted(self.edges):
            source_group = parent[source]
            destination_group = parent[destination]

            # Same group means this edge would create a cycle.
            if source_group != destination_group:
                minimum_spanning_tree.append((source, destination, weight))
                minimum_cost += weight

                # Merge the two groups after adding the edge.
                for vertex in range(self.num_vertices):
                    if parent[vertex] == destination_group:
                        parent[vertex] = source_group

                if len(minimum_spanning_tree) == self.num_vertices - 1:
                    break

        if len(minimum_spanning_tree) != self.num_vertices - 1:
            raise ValueError("A spanning tree does not exist for a disconnected graph")

        return minimum_spanning_tree, minimum_cost


if __name__ == "__main__":
    graph = KruskalAlgorithm(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)

    minimum_spanning_tree, minimum_cost = graph.kruskal()

    print("Edges in the Minimum Cost Spanning Tree:")
    for source, destination, weight in minimum_spanning_tree:
        print(f"{source} -- {destination} == {weight}")
    print("Minimum cost:", minimum_cost)
