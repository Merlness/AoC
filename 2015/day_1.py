def check_floor(moves): 
    floor = 0
    
    for move in moves:
        floor += translate_move(move)

    return floor

def translate_move(move):
    if move == '(':
        return 1
    return -1
    

def check_basement(moves):
    floor = 0
    floors_moved = 0
    
    for move in moves:
        floor += translate_move(move)
        floors_moved += 1
    
        if is_in_basement(floor):
            return floors_moved

def is_in_basement(floor):
    return floor == -1
