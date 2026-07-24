class PrimsAlgorithm:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0 for _ in range(num_vertices)]
                      for _ in range(num_vertices)]

    def prim(self, source=0):
        """Return the minimum spanning tree edges and their total cost."""
        if not 0 <= source < self.num_vertices:
            raise ValueError("Source vertex is outside the graph")

        selected = [False] * self.num_vertices
        selected[source] = True
        minimum_spanning_tree = []
        minimum_cost = 0

        # A spanning tree of V vertices contains exactly V - 1 edges.
        for _ in range(self.num_vertices - 1):
            minimum_weight = float("inf")
            start_vertex = -1
            end_vertex = -1

            # Find the cheapest edge from a selected vertex to an
            # unselected vertex.
            for source_vertex in range(self.num_vertices):
                if selected[source_vertex]:
                    for destination_vertex in range(self.num_vertices):
                        weight = self.graph[source_vertex][destination_vertex]

                        if (not selected[destination_vertex] and 0 < weight < minimum_weight):
                            minimum_weight = weight
                            start_vertex = source_vertex
                            end_vertex = destination_vertex

            if end_vertex == -1:
                raise ValueError("A spanning tree does not exist for a disconnected graph")

            selected[end_vertex] = True
            minimum_spanning_tree.append(
                (start_vertex, end_vertex, minimum_weight)
            )
            minimum_cost += minimum_weight

        return minimum_spanning_tree, minimum_cost


if __name__ == "__main__":
    graph = PrimsAlgorithm(4)
    graph.graph = [
        [0, 2, 6, 0],
        [2, 0, 9, 5],
        [6, 9, 0, 8],
        [0, 5, 8, 0]
    ]

    minimum_spanning_tree, minimum_cost = graph.prim(0)

    print("Edges in the Minimum Cost Spanning Tree:")
    for source, destination, weight in minimum_spanning_tree:
        print(f"{source} -- {destination} == {weight}")
    print("Minimum cost:", minimum_cost)
