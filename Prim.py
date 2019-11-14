
# graph class for graph object
class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, v_name):
        self.vertices.append(v_name)

    def add_edge(self, v1, v2, cost=0):
        new_edge = Edge(v1, v2, cost)
        self.edges.append(new_edge)


# Edge class for Edge object
class Edge:
    def __init__(self, v1, v2, cost=0):
        self.a = v1
        self.b = v2
        self.weight = cost

    def print_edge(self, g):
        print(g.vertices[self.a] + " to " + g.vertices[self.b] + " ~ " + str(self.weight))


def min_vertex(g, s, c):
    m = 100
    result = 0
    for n in range(0, len(g.vertices)):
        if s[n] == 0 and c[n] <= m:
            m = c[n]
            result = n
    return n


def prim(g):
    p = [-1, -1, -1, -1, -1, -1]
    c = [100, 100, 100, 100, 100, 100]
    s = [0, 0, 0, 0, 0, 0]

    # starts with vertex at index 0
    v = 0
    s[v] = 1
    tree = []

    for i in range(1, len(g.vertices)):
        adjacent = []
        for m in range(0, len(g.edges)):
            if g.edges[m].a == v or g.edges[m].b == v:
                adjacent.append(g.edges[m])
        for j in range(0, len(adjacent)):
            w = adjacent[j].b
            if s[w] == 0 and adjacent[j].weight <= c[w]:
                p[w] = v
                c[w] = adjacent[j].weight
                to_add = adjacent[j]
        v = min_vertex(g, s, c)
        s[v] = 1
        tree.append(to_add)
    for k in range(0, len(tree)):
        tree[k].print_edge(g)
    for m in range(0, len(s)):
        print(s[m])


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")

# A = 0, B = 1, C = 2, D = 3, E = 4, F = 5
graph.add_edge(0, 1, 7)
graph.add_edge(0, 3, 9)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 4, 1)
graph.add_edge(1, 5, 2)
graph.add_edge(2, 5, 6)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 5, 2)

prim(graph)
