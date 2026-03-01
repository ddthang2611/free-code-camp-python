
def dfs_n_queens(n):
    if n < 1:
        return []
    
    position_stack = [(0, 0)]
    board = [[0] * n for _ in range(n)]     
    result = []    
    
    for i in range(n):
        choices = []
        while position_stack:
            x, y = position_stack.pop()
            try: 
                board[x][y] = 1
                for j in range(-1, 1, 1):
                    if board[x+j][y+j] == 1 :
                        board[x][y] = 0
                    else:
                        choices.append(x)
            except IndexError:
                continue
            if y < n - 1:
                position_stack.append((i, y+1))
        if len(choices) == n:
            result.append(choices)
                
    return result
            
print(dfs_n_queens(4))
            
        
            