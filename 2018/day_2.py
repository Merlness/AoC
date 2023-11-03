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
    list_of_similar_letters = []

    for root_word in range(len(IDs)):
        # for next_word in range(root_word + 1, len(IDs)):
        #     similar_char = check_letters(IDs, root_word, next_word)
        #     list_of_similar_letters.append(similar_char)
        list_of_similar_letters += asd(root_word, IDs)

    return ''.join(max(list_of_similar_letters, key=len))


def asd(root_word, IDs):
    similar_letters = []
    for next_word in range(root_word + 1, len(IDs)):
        similar_char = check_letters(IDs, root_word, next_word)
        similar_letters.append(similar_char)

    return similar_letters

def check_letters(IDs, word, iterable_word):
    similar_char = []

    for char in range(len(IDs[word])):
        if IDs[word][char] == IDs[iterable_word][char]:
            similar_char.append(IDs[word][char])

    return similar_char
