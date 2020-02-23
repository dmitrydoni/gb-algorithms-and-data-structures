"""
Доработать алгоритм Дейкстры, чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""


def dijkstra(graph, start):
    vertex_0 = start
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    path = []  # list of vertices visited
    vertices = []  # list of paths

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

                    path.append(i)

        vertices.append(path)

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    print(f'Vertices: {vertices}')
    print(f'Costs from vertex {vertex_0} to other vertices: {cost}')


if __name__ == '__main__':

    # generate a directed and weighted graph
    g = [
        [0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 5, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0],
    ]

    start_vertex = int(input("Start with vertex: "))
    dijkstra(g, start_vertex)
