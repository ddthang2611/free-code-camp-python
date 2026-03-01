
def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return "The number of pairs should be an integer"
    
    if pairs < 1:
        return "The number of pairs should be at least 1"
    
    result = []
    queue = [("", 0, 0)]
    
    while queue:
        print(queue)
        queue.pop(0)
        current, opens_used, closes_used = queue.values()
    
    return result