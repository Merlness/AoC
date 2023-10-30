def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

directions = list(fetch_test_data('../test_data/2016/day_2.txt'))

coordinate_to_code = {
                        (0, 2): 1, 
                        (-1, 1): 2, 
                        (0, 1): 3, 
                        (1, 1): 4, 
                        (-2, 0): 5, 
                        (-1, 0): 6, 
                        (0, 0): 7, 
                        (1, 0): 8, 
                        (2, 0): 9, 
                        (-1, -1): 'A',  
                        (0, 1): 'B', 
                        (1, -1):'C', 
                        (0, -2): 'D', 
                        }


def decoder(instructions):
    return [coordinate_to_code[find_coordinate(move)] for move in instructions]

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

def set_boundary(x, y, a, b):
    if (x,y) in [(-1,2), (1,2), (-2,1), (2,1), (-2,-1), (2,-1), (-1,-2), (1,-2), (0,3), (0,-3), (3,0), (-3,0)]:
        x = a
        y = b
    
    return x, y 

def find_coordinate(move):
    x = -2
    y = 0
    
    for letter in move:
        [x, y] = move_coordinates(x, y, letter)
    
    return x, y

def move_coordinates(x, y, letter):
    a = x
    b = y
    
    [x, y] = translate_letters(x, y, letter)
    [x, y] = set_boundary(x, y, a, b)
    return x, y



print(decoder(directions))