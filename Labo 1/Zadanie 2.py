from collections import deque

graph = {
    "1" : ['2'],
    "2" : ['1', '3', '4'],
    "3" : ['2'],
    "4" : ['2', '5', '6'],
    "5" : ['4'],
    "6" : ['4', '7'],
    "7" : ['6']
}

def BFS(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)

    return  None

print(BFS(graph, '1', '6'))