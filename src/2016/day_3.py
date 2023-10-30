import re
def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    text_ints = [ int(x) for x in text.split() ]
    file.close()
    return text_ints 

triplets = fetch_test_data('../test_data/2016/day_3.txt')
triangles = [triplets[third:third+3] for third in range(0, len(triplets), 3)]

def find_possible_triangles(tri_list):
    potential_triangles = 0
    for triangle in tri_list:
        potential_triangles = compare_side_and_2sides(potential_triangles, triangle)

    return potential_triangles

def make_new_triangles():
    flat_array = make_flat_array()
    new_triangles = [flat_array[third:third+3] for third in range(0, len(flat_array), 3)]

    return new_triangles

def compare_side_and_2sides(potential_triangles, triangle):
    if max(triangle) < sum(triangle)- max(triangle):
        return potential_triangles + 1

    return potential_triangles

def make_flat_array():
    faux_triangles = triangles.copy()
    flat_array = []

    while faux_triangles:
        convert_list_to_array(flat_array, faux_triangles)
    
    return flat_array

def convert_list_to_array(flat_array, faux_triangles):
    for fake_tri in faux_triangles:
        if fake_tri:  
            flat_array.append(fake_tri.pop(0))
        else:
            faux_triangles.remove(fake_tri)



print(find_possible_triangles(triangles))
print (find_possible_triangles(make_new_triangles()))
print (find_possible_triangles(make_new_triangles()))

