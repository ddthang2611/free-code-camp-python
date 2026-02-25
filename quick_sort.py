
def quick_sort(list):
    if len(list) == 0:
        return []
    
    pivot = list[-1]
    left_sublist = []
    equal_sublist = []
    right_sublist = []
    
    for i in range(len(list)):
        if list[i] < pivot:
            left_sublist.append(list[i])
        elif list[i] == pivot: 
            equal_sublist.append(list[i])
        elif list[i] > pivot:
            right_sublist.append(list[i])
    
    left_sublist = quick_sort(left_sublist)
    right_sublist = quick_sort(right_sublist)
    
    return left_sublist + equal_sublist + right_sublist
        
    