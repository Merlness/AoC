import re
from collections import Counter
#part 1
def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

# def format_test_data(lines):
#     return [int(s) for s in re.findall(r'\d+', lines)]

# dimensions_list = [format_test_data(x) for x in fetch_test_data('../test_data/2015/day_2.txt')]
santa_directions = list(fetch_test_data('../test_data/2015/day_3.txt'))

def santa_coordinates(directions):
    x = 0
    y = 0
    coordinates = [(x,y)]
    for moves in directions:
        if moves == '^':
            y += 1
            coordinates.append((x,y))
        elif moves == 'v':
            y -= 1
            coordinates.append((x,y))
        elif moves == '>':
            x += 1
            coordinates.append((x,y))
        elif moves == '<':
            x -= 1
            coordinates.append((x,y))
    return set(coordinates)

def robo_santa_coordinates(directions):
    x = 0
    y = 0
    a = 0
    b = 0

    coordinates = [(x,y)]
    temp1 = []
    temp2 = []

    for i in range(len(directions)):
        if i % 2 ==0:
            temp1.append(directions[i])
        else:
            temp2.append(directions[i])

    for moves in temp1:
        if moves == '^':
            y += 1
            coordinates.append((x,y))
        elif moves == 'v':
            y -= 1
            coordinates.append((x,y))
        elif moves == '>':
            x += 1
            coordinates.append((x,y))
        elif moves == '<':
            x -= 1
            coordinates.append((x,y))

    for moves in temp2:
        if moves == '^':
            b += 1
            coordinates.append((a,b))
        elif moves == 'v':
            b -= 1
            coordinates.append((a,b))
        elif moves == '>':
            a += 1
            coordinates.append((a,b))
        elif moves == '<':
            a -= 1
            coordinates.append((a,b))

    return set(coordinates)

santa_coordinates_list = robo_santa_coordinates(santa_directions)


print(len(santa_coordinates_list))
print(len(santa_coordinates(santa_directions)))


