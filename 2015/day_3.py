import re
from collections import Counter
#part 1
def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

santa_directions = list(fetch_test_data('../test_data/2015/day_3.txt'))

def count_santa_visits(directions):
    return len(set(manage_coordinates_of(directions)))

def count_robo_santa_visits(directions):
    [santa, robo] = test(directions)
    return len(set(manage_coordinates_of(santa) + manage_coordinates_of(robo)))

def convert_arrows(row, column, pointers):
    row = 0
    column = 0
    if pointers == '^':
        row += 1
    elif pointers == 'v':
        row -= 1
    elif pointers == '>':
        column += 1
    elif pointers == '<':
        column -= 1
    return row, column

def manage_coordinates_of(directions):
    x = 0
    y = 0
    coordinates = [(0, 0)]

    for moves in directions:
        [y_difference, x_difference] = convert_arrows(y, x, moves)
        x += x_difference
        y += y_difference
        coordinates.append((x, y))

    return coordinates

def test(directions):
    santa = []
    robo = []
    for every_other in range(len(directions)):
        if every_other % 2 == 0:
            santa.append(directions[every_other])
        else:
            robo.append(directions[every_other])

    return santa, robo

print(count_santa_visits(santa_directions))
print(count_robo_santa_visits(santa_directions))