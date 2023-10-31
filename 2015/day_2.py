def part_1(dimensions):
    return sum_by(dimensions, find_wrapping_paper)

def find_sides(dimension):
    [length, width, height] = dimension

    sides = [2 * length * width,
            2 * width * height,
            2 * height * length]
    sides.sort()

    return sides

def find_wrapping_paper(dimension):
    sides = find_sides(dimension)
    shortest_side = sides[0] / 2

    return sum(sides) + shortest_side

def part_2(dimensions):
    return sum_by(dimensions, find_ribbon_length)

def add_ribbon_sides(dimension):
    dimension.sort()

    short_side_1 = dimension[0]
    short_side_2 = dimension[1]

    return 2 * (short_side_1 + short_side_2)

def find_ribbon_bow(dimension):
    ribbon_bow = 1

    for length in dimension:
        ribbon_bow = ribbon_bow * length  

    return ribbon_bow

def find_ribbon_length(dimension):
    ribbon_side_length = add_ribbon_sides(dimension)
    ribbon_bow = find_ribbon_bow(dimension)

    return ribbon_side_length + ribbon_bow

def sum_by(collection, measure):
    total = 0
    
    for item in collection:
        total += int(measure(item))

    return total