import re
def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    text_ints = [ int(x) for x in text.split() ]
    file.close()
    return text_ints 

triplets = fetch_test_data('../test_data/2016/day_3.txt')
triangles = [triplets[third:third+3] for third in range(0, len(triplets), 3)]

def possible_triangles(tri_list):
    potential_triangles = 0
    for triangle in tri_list:
        if max(triangle) < sum(triangle)- max(triangle):
                potential_triangles += 1

    return potential_triangles


def sorting():
    faux_triangles = triangles
    flat_array = []

    while faux_triangles:
        for fake_tri in faux_triangles:
            if fake_tri:  
                flat_array.append(fake_tri.pop(0))
            else:
                faux_triangles.remove(fake_tri)

    new_triangles = [flat_array[third:third+3] for third in range(0, len(flat_array), 3)]
    return new_triangles


print(possible_triangles(triangles))
print (possible_triangles(sorting()))






# print(possible_triangles(triangles))

# print(test)

# test= [[1,2,3], [5,12,13], [5, 10, 25], [1, 2, 2]]


# def fetch_test_data_2(path):
#     file = open(path, "r")
#     text = file.read()
#     file.close()
#     return text

# test = fetch_test_data_2('../test_data/2016/test.txt')