import re
from collections import Counter
#part 1
def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

santa_directions = list(fetch_test_data('../test_data/2015/day_3.txt'))

def santa_coordinates(directions):
    x = 0
    y = 0
    coordinates = set((x,y))
    
    for moves in directions:
        if moves == '^':
            y += 1
        elif moves == 'v':
            y -= 1
        elif moves == '>':
            x += 1
        elif moves == '<':
            x -= 1
        coordinates.add((x,y))

    return coordinates

def robo_santa_coordinates(directions):
    x = 0
    y = 0
    a = 0
    b = 0

    coordinates = [(x,y)]
    santa = []
    robo = []

    for every_other in range(len(directions)):
        if every_other % 2 ==0:
            santa.append(directions[every_other])
        else:
            robo.append(directions[every_other])

    for moves in santa:
        if moves == '^':
            y += 1
        elif moves == 'v':
            y -= 1
        elif moves == '>':
            x += 1
        elif moves == '<':
            x -= 1
        coordinates.append((x,y))

    for moves in robo:
        if moves == '^':
            b += 1
        elif moves == 'v':
            b -= 1
        elif moves == '>':
            a += 1
        elif moves == '<':
            a -= 1
        coordinates.append((a,b))

    return set(coordinates)

santa_coordinates_list = robo_santa_coordinates(santa_directions)

print(len(santa_coordinates_list))
print(len(santa_coordinates(santa_directions)))


