def part_1(instructions):
    cardinal_direction = 90
    x = 0
    y= 0

    for instruction in instructions:
        cardinal_direction = change_direction(cardinal_direction, instruction)
        [x, y] = change_distance(x, y, cardinal_direction, instruction)
    
    return abs(x) + abs(y)

def change_direction(cardinal_direction, instruction):
    if instruction[0] == 'R':
        cardinal_direction -=90
    else:
        cardinal_direction += 90

    if abs(cardinal_direction) == 360:
        cardinal_direction = 0
    
    return cardinal_direction

def change_distance(x, y, cardinal_direction, instruction):
    if cardinal_direction == 90 or cardinal_direction == -270:
        y += int(instruction[1:])
    elif cardinal_direction == 270 or cardinal_direction == -90:
        y -= int(instruction[1:])
    elif abs(cardinal_direction) == 180:
        x -= int(instruction[1:])
    elif cardinal_direction == 0:
        x += int(instruction[1:])
    
    return x, y

def part_2(instructions):
    cardinal_direction = 90
    x = 0
    y= 0
    coordinates = [(x, y)]

    for instruction in instructions:
        a = x
        b = y
        cardinal_direction = change_direction(cardinal_direction, instruction)
        [x, y] = change_distance(x, y, cardinal_direction, instruction)




def tracking():
    points = [(0, 0), (-8, 0)]
    coordinates = []
    for coordinate in points:
        x = points[-2][0]
        y = points[-2][1]
        a = points[-1][0]
        b = points[-1][1]

        change_in_x = x + a
        change_in_y = y + b
        total_change = abs(change_in_x) + abs(change_in_y)

        for piece in range(total_change + 1):
            if change_in_x != 0:
                if change_in_x > 0:
                    temp = x + piece
                    if (temp, y) in coordinates:
                        return print(abs(temp) + abs(y))
                    coordinates.append((temp, y))



                else:
                    temp = x - piece
                    # if (temp, y) in coordinates:
                    #     return print(abs(temp) + abs(y))

                    coordinates.append((temp, y))





# - - - - - - - -
#       -       -
#       -       -
#       -       -
#       - - - - -

# def part_2(instructions):
#     cardinal_direction = 90
#     x = 0
#     y= 0
#     coordinates = [(x, y)]

#     for instruction in instructions:
#         a = x
#         b = y
#         cardinal_direction = change_direction(cardinal_direction, instruction)
#         [x, y] = change_distance(x, y, cardinal_direction, instruction)
        
#         coordinate_distance_x = abs(abs(x) - abs(a))
#         coordinate_distance_y = abs(abs(y) - abs(b))
#         coordinate_distance = coordinate_distance_y + coordinate_distance_x
        
#         for distance in range(1, coordinate_distance + 1):
#             if coordinate_distance_x > 0:
#                 if

#                 if (a + distance, b) in coordinates:
#                     return abs(a) + abs(b)

#                 coordinates.append((a + distance, b))

#             else:
#                 if (a, b + distance) in coordinates:
#                     return abs(a) + abs(b)
#                 coordinates.append((a, b + distance))

        # if (x, y) in coordinates:
        #     return abs(x) + abs(y)

        # coordinates.append((x,y))
