
def dfs_n_queens(n):
    if n < 1:
        return []
    
    result = []
    
    def check_safe(x, y, choices):
        for i, j in enumerate(choices):
            if y == j or abs(x - i) == abs(y - j):
                return False  
        return True
        
    position = [(0, 0, [])]
    
    while position:
        x, y, choices = position.pop()
            
        if y < n - 1:
            position.append((x, y + 1, choices))    
            
        if check_safe(x, y, choices):
            new_choices = choices + [y]
            if x == n - 1:
                result.append(new_choices)
            else:
                position.append((x + 1, 0, new_choices))
    
    return result
  
print(dfs_n_queens(4))
            
        
            