import numpy as np

File_data = np.loadtxt("../test_data/2017/day_2.txt", dtype=int) 

max_element_row = np.max(File_data, 1)
min_element_row = np.amin(File_data, 1)

total_difference = sum(max_element_row) - sum(min_element_row)

def find_sum_of_quotients(array):
    result= 0
    
    for row in array:
        result = add_result_of_row(result, row)

    return result


def find_quotients_of_row(row, numerator, result):
    for divider in row:
        if numerator % divider == 0 and (numerator / divider) > 1 :
            return result + int(numerator / divider)
        
    return result

def add_result_of_row(result, row):
    for numerator in row:
        result = find_quotients_of_row(row, numerator, result)

    return result

print(find_sum_of_quotients(File_data))
print(total_difference)