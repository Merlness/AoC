import re
from collections import Counter

instructions= 'R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3'

instructions_list = instructions.split(", ")
test_list = ['R5', 'L5', 'R5', 'R188']


def shorten_path( directions):
    degrees = 90
    x = 0
    y = 0
    direction = []
    distance = []
    coordinates = [(x,y)]
    for movement in directions:
        direction.append(movement[0])
        distance.append(int(movement[1:]))
        # print(direction, distance, len(distance)-1)
        correction = len(distance) -1
        
        if direction[correction] == 'R':
            degrees -= 90
        elif direction[correction] == 'L':
            degrees += 90
        
        
        if degrees == 360 or degrees == -360:
            degrees = 0
        
        if degrees == 0:
            x += distance[correction]
        elif degrees == 90 or degrees == -270:
            y += distance[correction]
        elif degrees == 180 or degrees == -180:
            x -= distance[correction]
        elif degrees == 270 or degrees == -90:
            y -= distance[correction]
    return print(abs(x)+abs(y))


shorten_path(instructions_list)

# print(instructions_list)