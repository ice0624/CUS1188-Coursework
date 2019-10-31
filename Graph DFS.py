graph = {"A" : ["B", "D"], "B" : ["A", "C", "E", "F"], "C" : ["B", "F"], "D" : ["A", "E"], "E" : ["B", "D", "F"], "F" : ["B", "C", "E"]}
visited = {"A" : False, "B" : False, "C" : False, "D" : False, "E" : False, "F" : False}

def dfs(g, v):
    visited[v] = True
    print(v)
    for w in graph[v]:
        if visited[w] == False:
            dfs(graph, w)

dfs(graph, "A")
end_values = visited.values()
print(end_values)