
def selection_sort(list):
    if len(list) == 0:
        return []
    
    for i in range(len(list)):
        min_value = list[i]
        for j in range(i, len(list), 1):
            if list[j] < min_value:
                min_value = list[j]
                list[i], list[j] = list[j], list[i]

    return list

print(selection_sort([33, 1, 89, 2, 67, 245]))