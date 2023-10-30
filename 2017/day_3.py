# import math

# # def get_distance(number):
#     # old_square = 0
#     # new_square = 0
# def get_root(number):
#     for s_root in range(number+1):
#         s_root = 1
#         root_list = []
#         while number > s_root*s_root :
#             s_root += 2
#             root_list.append(s_root)
#     return root_list

# print(get_root(50))
# get_root(10)[-2]

#     #     else:
#     #         old_square = (s_root-2) * (s_root-2)
#     #         new_square = s_root * s_root
#     #         perimeter = new_square - old_square
#     #         corners_separated_by = perimeter/4
#     #         corners = [old_square + corners_separated_by, 
#     #                    old_square + 2 * corners_separated_by, 
#     #                    old_square + 3 * corners_separated_by,
#     #                    new_square,
#     #                    old_square]
           
#     #         min_distance = len(root_list)
#     #         max_distance = int(2 * min_distance)
        
#     #         possibilities = [abs(number -corners[0]),
#     #                              abs(number - corners[1]),
#     #                              abs(number - corners[2]),
#     #                              abs(number - corners[3]),
#     #                              abs(number - corners[4])]
#     #         possibilities.sort()
#     #         distance = int(max_distance - possibilities[0])
#     # return distance
    

# # print(get_distance(277678))
# ########


import math

def get_distance(number):   
    [s_root, boxes_away_from_center] = find_square_roots(number)
    corners = find_corners(s_root)

    max_distance = find_max_distance(boxes_away_from_center)
    distance_to_corner = find_distance_to_corner(number, corners)

    return int(max_distance - distance_to_corner)

def find_square_roots(number):
    for s_root in range(number+1):
        s_root = 1
        boxes_away_from_center = []
        while number > s_root*s_root :
            s_root += 2
            boxes_away_from_center.append(s_root)

    return s_root, boxes_away_from_center

def find_corners(s_root):
    old_square = (s_root-2) * (s_root-2)
    new_square = s_root * s_root
    perimeter = new_square - old_square
    corners_separated_by = perimeter/4

    corners = []
    for width in range(5):
        corners.append(old_square + (width * corners_separated_by))
    
    return corners

def find_max_distance(boxes_away_from_center):
    min_distance = len(boxes_away_from_center)
    max_distance = int(2 * min_distance)

    return max_distance

def find_distance_to_corner(number, corners):
    possibilities = []
   
    for corner in corners:
        possibilities.append(abs(number - corner))
    possibilities.sort()

    return possibilities[0]




print(get_distance(277678))