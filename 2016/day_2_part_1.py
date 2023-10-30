def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

directions = list(fetch_test_data('../test_data/2016/day_2.txt'))

coordinate_to_number = {
                        (-1, 1): 1,
                        (0, 1): 2,
                        (1, 1): 3,
                        (-1, 0): 4,
                        (0, 0): 5,
                        (1, 0): 6,
                        (-1, -1): 7,
                        (0, -1): 8,
                        (1, -1): 9,
                        }

def decoder(instructions):
    return [coordinate_to_number[find_coordinate(move)] for move in instructions]

def translate_letters(x, y, letter):
    if letter == 'U':
        y += 1
    elif letter == 'D':
        y -= 1
    elif letter == 'R':
        x += 1
    elif letter == 'L':
        x -= 1
    return x, y

def set_boundaries(x, y):
    if x == 2:
        x = 1
    if x == -2:
        x = -1
    if y == 2:
        y = 1
    if y == -2:
        y = -1

    return x, y

def find_coordinate(move):
    x = 0
    y = 0
    
    for letter in move:
        [x, y] = move_coordinates(x, y, letter)
    
    return x, y

def move_coordinates(x, y, letter):
    [x, y] = translate_letters(x, y, letter)
    return set_boundaries(x, y)

print(decoder(directions))