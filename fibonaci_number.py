
def fibonacci(n):
    sequence = [0, 1]
    
    if n < 2:
        return sequence[n]  
    else:
        for i in range(n):
            if i >= len(sequence):
                new_value = sequence[i-1] + sequence[i-2]
                sequence.append(new_value)
                
            if len(sequence) == n:
                print(sequence)
                return sequence[n-1] + sequence[n-2]
    
print(fibonacci(0))

