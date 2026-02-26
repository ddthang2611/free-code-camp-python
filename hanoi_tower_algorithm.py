

def hanoi_solver(disk_number):
    first_tower = list(range(disk_number, 0, -1))
    second_tower = []
    third_tower = []
    first_line = f"{first_tower} {second_tower} {third_tower}\n"
    final_result = []
    final_result.append(first_line)
    
    def move_disk(src_tower, des_tower):
        if len(src_tower) > 0:
            des_tower.append(src_tower.pop())
        new_line = f"{first_tower} {second_tower} {third_tower}\n"
        final_result.append(new_line)
    
    def resolve_disk(n, src_tower, des_tower, aux_tower):
        if n == 1:
            move_disk(src_tower, des_tower)
        else:
            resolve_disk(n -1, src_tower, aux_tower, des_tower)
            move_disk(src_tower, des_tower)
            resolve_disk(n - 1, aux_tower, des_tower, src_tower)

    resolve_disk(disk_number, first_tower, third_tower, second_tower)
    result = "".join(final_result)
    result = result[:-1]
    
    return result
    
print(hanoi_solver(3))