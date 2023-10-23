import numpy as np

File_data = np.loadtxt("../test_data/2017/day_2.txt", dtype=int) 

max_element_row = np.max(File_data, 1)
min_element_row = np.amin(File_data, 1)

# test = np.array([[5, 2, 9, 8], [7, 9, 3, 4], [3, 5, 6, 8]])
# min_test =np.amin(test, 1)
# max_test= np.max(test, 1)

total_difference = sum(max_element_row) - sum(min_element_row)

def check_division(array):
    add_result= 0
    
    for row in array:
        for numerator in row:
            for divider in row:
                if numerator % divider == 0 and (numerator / divider) > 1 :
                    add_result += int(numerator / divider)
                if len(row) != len(set(row)):
                    add_result += len(row) - len(set(row))
    return add_result

print(check_division(File_data))
