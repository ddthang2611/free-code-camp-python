

def number_pattern(n):
    final_result = ""
    
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    for i in range(n):
        if i == 0:
            final_result += (str(i+1))
        else:
            final_result += (" " + str(i + 1))
            
    return final_result

print(number_pattern("done"))