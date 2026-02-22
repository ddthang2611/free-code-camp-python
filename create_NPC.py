full_dot = '●'
empty_dot = '○'

def calculate_strength(point):
    strength_point = "STR "
    
    for i in range(10):
        if point > 0:
            strength_point += full_dot
        else:
            strength_point += empty_dot
        point -= 1
    return strength_point

def calculate_intelligence(point):
    intelligence_point = "INT "
    for i in range(10):
        if point > 0:
            intelligence_point += full_dot
        else:
            intelligence_point += empty_dot
        point -= 1
    return intelligence_point

def calculate_charisma(point):
    charisma_point = "CHA "
    for i in range(10):
        if point > 0:
            charisma_point += full_dot
        else:
            charisma_point += empty_dot
        point -= 1
    return charisma_point

def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    
    for i in name:
        if i == " ":
            return "The character name should not contain spaces"
    
    if not isinstance(strength, int):
        return "All stats should be integers"
    elif not isinstance(intelligence, int):
        return "All stats should be integers"
    elif not isinstance(charisma, int):
        return "All stats should be integers"
    
    if not strength <= 4 or not intelligence <= 4 or not charisma <= 4:
        return "All stats should be no more than 4"
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    total_point = strength + intelligence + charisma
    if total_point != 7:
        return "The character should start with 7 points"
    
    strength_point = calculate_strength(strength)
    intelligence_point = calculate_intelligence(intelligence)
    charisma_point = calculate_charisma(charisma)

    result = name + "\n" + strength_point + "\n" + intelligence_point + "\n" + charisma_point
    print("done")
    return result

create_character("ren", 4, 2, 1)

