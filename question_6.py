def has_cycle(graph):
    def dfs(node, visited, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True
        for neighbor in graph.get(node, []):
            if recursion_stack[neighbor]:
                return True
            if not visited[neighbor] and dfs(neighbor, visited, recursion_stack):
                return True
        recursion_stack[node] = False
        return False
    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}
    for node in graph:
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True
    return False



graph = {
0: [1],
1: [2],
2: [3],
3: [0]
}


print(has_cycle(graph))