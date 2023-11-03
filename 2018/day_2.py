import collections

def part_1(IDs):
    count_list = []
    twos= 0
    threes = 0

    for id in IDs:
        count_list = find_twos_threes(id, count_list)
        [twos, threes] = calculate_twos_threes(twos, threes, count_list)
        count_list = []
    return twos * threes

def find_twos_threes(IDs, count_list):
    for item in range(len(IDs)):
        count_list.append(IDs.count(IDs[item]))

    return count_list

def calculate_twos_threes(twos, threes, count_list):
    if 2 in count_list:
        twos += 1
    if 3 in count_list:
        threes +=1
    
    return twos, threes


def part_2(IDs):
    rest_of_IDs = IDs[1:]
    for id in IDs:
        for check_id in rest_of_IDs:
             if is_off_by_one(id, check_id):
                return similar_chars(id, check_id)

    return False
   

def is_off_by_one(id, check_id):
    one_off_length = len(id) - 1
    if is_only_one_difference(id, check_id):
        if is_in_correct_order(id, check_id):
            return True

    return False

def similar_chars(id, check_id):
    one_off_length = len(id) - 1
    word = []

    for char in range(one_off_length + 1):
        if id[char] == check_id[char]:
            word.append(id[char])

    return ''.join(word)

def is_only_one_difference(id, check_id):
    result = collections.Counter(id) & collections.Counter(check_id)
    intersected_list = list(result.elements())
    one_off_length = len(id) - 1

    if len(intersected_list) == one_off_length:
        return True
    return False    

def is_in_correct_order(id, check_id):
    one_off_length = len(id) - 1
    perfect_match = 0

    for char in range(one_off_length + 1):
        if id[char] == check_id[char]:
            perfect_match += 1
    
    if perfect_match == one_off_length:
        return True
    
    return False
