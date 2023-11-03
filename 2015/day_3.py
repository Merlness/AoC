def part_1(directions):
    x = 0
    y = 0
    coordinates = [(x, y)]

    for move in directions:
        [x, y] = decifer_move(move, x, y)
        coordinates.append((x, y))

    return len(set(coordinates))

def decifer_move(move, x, y):
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '>':
        x += 1
    elif move == '<':
        x -= 1

    return x, y

def part_2(directions):
    x = 0
    y = 0
    a = 0
    b = 0
    santas_turn = True
    coordinates = [(x, y)]

    for move in directions:
        if santas_turn:
            [x, y] = decifer_move(move, x, y)
            coordinates.append((x, y))
        
        else:
            [a, b] = decifer_move(move, a, b)
            coordinates.append((a, b))
            
        santas_turn = not santas_turn

    return len(set(coordinates))

