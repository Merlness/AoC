import re
from collections import Counter
#part 1
def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

santa_directions = list(fetch_test_data('../test_data/2015/day_3.txt'))
#change verbs -ing
def converting_coordinates(row, column, pointers):
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
#change test
def test(directions):
    x = 0
    y = 0
    coordinates = [(0, 0)]

    for moves in directions:
        [y_difference, x_difference] = converting_coordinates(y, x, moves)
        x += x_difference
        y += y_difference
        coordinates.append((x, y))

    return coordinates

def counting_santa_visits(directions):
    return len(set(test(directions)))

def counting_robo_santa_visits(directions):
    santa = []
    robo = []
#put these into a function and come out with a vector like above
    for every_other in range(len(directions)):
        if every_other % 2 == 0:
            santa.append(directions[every_other])
        else:
            robo.append(directions[every_other])
  
    return len(set(test(santa) + test(robo)))

print(counting_santa_visits(santa_directions))
print(counting_robo_santa_visits(santa_directions))