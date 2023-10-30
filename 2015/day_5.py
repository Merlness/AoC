import re

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

all_words = list(fetch_test_data('../test_data/2015/day_5.txt'))

def find_nice_words(words):
    count = 0

    for word in words:
        if is_nice(word):
            count += 1

    return count

def find_newer_nice_words(words):
    count = 0

    for word in words:
        if is_new_nice(word):
            count += 1
    
    return count

def check_nice_one(word):
    for bad_letters in ['xy','ab','cd','pq']:
            if word.find(bad_letters) >= 0:
                return False    
    return True

def check_nice_two(word):
    if len(re.findall(r'a|e|i|o|u', word)) > 2:
            return True
    else: 
        return False

def check_nice_three(word):
    for character in range(len(word)):
        if word[character] == word[character-1] and character!= 0:
            return True
    return False

def help_new_nice_one(word):
    for letter_repeats in range(len(word)):
        if word[letter_repeats] == word[letter_repeats -2] and letter_repeats > 1:
            return True
    return False

def check_new_nice_one(word):
    return help_new_nice_one(word)

def help_new_nice_two(word):
    for first_pair in range(len(word)):
        for second_pair in range(first_pair + 2, len(word)-1):
            if [word[first_pair], word[first_pair + 1]] == [word[second_pair], word[second_pair+1]]:
                return True
    return False 

def check_new_nice_two(word):
    return help_new_nice_two(word)

def is_nice(word):
    return check_nice_one(word) and check_nice_two(word) and check_nice_three(word)     

def is_new_nice(word):
    return check_new_nice_one(word) and check_new_nice_two(word)

print(find_nice_words(all_words))
print(find_newer_nice_words(all_words))