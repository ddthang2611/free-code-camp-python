adj_matrix = [
    [0, 1, 0, 0], 
    [1, 0, 1, 0], 
    [0, 1, 0, 1], 
    [0, 0, 1, 0]
]

def dfs(adj_matrix, node_label):
    
    visit_stack = [node_label]
    visited = []
    visited.append(node_label)
    
    while visit_stack:
        current = visit_stack.pop()
        for i in range(len(adj_matrix[current])):
            if adj_matrix[current][i] == 1 and i not in visited:
                visit_stack.append(i)
                visited.append(i)
    
    return visited
    
print(dfs(adj_matrix, 1))
                