import re
from collections import Counter

instructions= 'R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3'

instructions_list = instructions.split(", ")

def find_distance( directions):
    degrees = 90
    x = 0
    y = 0

    for movement in directions:
        direction = movement[0]
        distance = int(movement[1:])
        
        degrees = change_direction(degrees, direction)      
        [x, y] = move(x, y, degrees, distance)

    return abs(x) + abs(y)

def change_direction(degrees, direction):
    if direction == 'R':
        degrees -= 90
    else:
        degrees += 90
    
    if degrees == 360 or degrees == -360:
        degrees = 0

    return degrees

def move(x, y, degrees, distance):
    if degrees == 0:
        x += distance
    elif degrees == 90 or degrees == -270:
        y += distance
    elif degrees == 180 or degrees == -180:
        x -= distance
    elif degrees == 270 or degrees == -90:
        y -= distance

    return x, y

print(find_distance(instructions_list))