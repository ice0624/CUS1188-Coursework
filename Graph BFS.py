import queue

graph = {"A" : ["B", "C", "D"], "B" : ["E"], "C" : ["F"], "D" : ["G"], "E" : ["D"], "F" : ["B"], "G" : ["C"]}
visited = {"A" : False, "B" : False, "C" : False, "D" : False, "E" : False, "F" : False, "G" : False}

def bfs(g, v, visited):
    q = queue.Queue(0)
    visited[v] = True
    print(v)
    q.put(v)

    while(q.empty() == False):
        w = q.get()
        visited[w] = True
        for u in g[w]:
            if visited[u] == False:
                visited[u] = True
                print(u)
                q.put(u)


bfs(graph, "A", visited)
end_values = visited.values()
print(end_values)
