# import numpy as np

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

text_of_changes = list(fetch_test_data('../test_data/2018/day_1.txt'))

def change_frequency(list_to_change):
    result = 0
    for frequency_changes in list_to_change:
        plus_minus_sign = frequency_changes[0]
        frequency = int(frequency_changes[1:])

        if plus_minus_sign == '+':
            result += frequency
        else:
            result -= frequency
    return result



def check_doubles(check_list):
    result = 0
    list_of_frequencies = []
    

    for frequency_changes in check_list:
        plus_minus_sign = frequency_changes[0]
        frequency = int(frequency_changes[1:])
                
        if plus_minus_sign == '+':
            result += frequency
        else:
            result -= frequency
                   
        list_of_frequencies.append(result)

    doubles_check = set(list_of_frequencies)
    #[item for item in list_of_frequencies if item not in doubles_check]

    return print(len(list_of_frequencies)), print(len(doubles_check)), print(list_of_frequencies)



test1 = ['+3', '+3', '+4', '-2', '-4'] #first reaches 10 twice.
test2 = ['-6', '+3', '+8', '+5', '-6']#first reaches 5 twice.
test3 = ['+7', '+7', '-2', '-7', '-4'] #first reaches 14 twice.

check_doubles(test2)

# print(text)


# change strings to numbers
# create a 'sum' =0
# read first symbol frequency_change[0] 
# if frequency_change[0] == + then sum += frequency_change[1:]
# else sum -= frequency_change[1:]
# return 
#
#

#
#
#
