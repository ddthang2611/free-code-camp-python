
def verify_card_number(card_number):
    card_number = card_number.replace('-', '').replace(' ', '')
    # print(card_number)
    
    check_digit = int(card_number[-1])
    print(check_digit)
    check_list = card_number[:-1:]
    char_list = []
    
    for char in check_list:
        # print(i)
        char_list.append(int(char))
    
    char_list.reverse()
    check_sum = check_digit
    for i in range(len(char_list)):
        if i % 2 == 0:
            char_list[i] = 2 * char_list[i]
            if char_list[i] > 9:
                char_list[i] -= 9
        check_sum += char_list[i]
    
    print(char_list)
    
    print(check_sum)
    if check_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
    
print(verify_card_number('4111-1111-1111-1111'))
