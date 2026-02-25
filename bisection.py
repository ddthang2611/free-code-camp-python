

def square_root_bisection(number, tolerance = 0.01, iter_num = 50):
    
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    lower_bound = 0
    upper_bound = max(1, number)
    mid = (lower_bound + upper_bound) / 2
    
    for i in range(iter_num):
        if pow(mid, 2) >= number:
            upper_bound = mid
            mid = (lower_bound + upper_bound) / 2
        else:
            lower_bound = mid
            mid = (lower_bound + upper_bound) / 2
            
        if upper_bound - lower_bound < tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        
        if i == iter_num - 1:
            print(f"Failed to converge within {iter_num} iterations")
            return None
    
    


print(square_root_bisection(0.001, 1e-7, 50))
