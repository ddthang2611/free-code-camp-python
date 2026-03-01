matrix_dict = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

def adjacency_list_to_matrix(matrix_dict):
    row = len(matrix_dict)
    result = [[0] * row for _ in range(row)]
    
    for x in matrix_dict.keys():
        for i in matrix_dict[x]:
            result[x][i] = 1
            
    for line in result:
        print(f"{line}\n")
    
    return result

adjacency_list_to_matrix(matrix_dict)