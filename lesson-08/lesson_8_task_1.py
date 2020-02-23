"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
"""


def count_handshakes(n):

    if n < 2:
        print("Nobody to shake hands here :(")
        return

    # generate lists for vertices (1 vertex = 1 friend) and edges (1 edge = 1 handshake)
    graph_vertices = [_ for _ in range(n)]
    print(f'List of friends: {graph_vertices}')
    graph_edges = []

    for i in range(len(graph_vertices)):
        current_vertex = graph_vertices.pop(0)
        print(f'Friend {current_vertex} shakes hands with new friends {graph_vertices}')

        for vertex in graph_vertices:
            graph_edges.append((current_vertex, vertex))

    print(f'Handshakes: {graph_edges}')
    print(f'Total handshakes: {len(graph_edges)}')


if __name__ == '__main__':
    n = int(input("How many friends? "))
    count_handshakes(n)
