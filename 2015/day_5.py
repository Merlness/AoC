import re

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

all_words = list(fetch_test_data('../test_data/2015/day_5.txt'))

#shorten function names
def finding_nice_words_rule_1(word):
    for bad_letters in ['xy','ab','cd','pq']:
            if word.find(bad_letters) >= 0:
                return False    
    return True

def finding_nice_words_rule_2(word):
    if len(re.findall(r'a|e|i|o|u', word)) > 2:
            return True
    else: 
        return False

def finding_nice_words_rule_3(word):
    for c in range(len(word)):
        #change
        if word[c] == word[c-1] and c!= 0:
            return True
    return False

def finding_newer_nice_words_rule_one(word):
    for letter_repeats in range(len(word)):
        #change
        if word[letter_repeats] == word[letter_repeats -2] and letter_repeats > 1:
            return True
    return False

def finding_newer_nice_words_rule_two(word):
    for letters_repeat in range(len(word)):
        for repetition in range(letters_repeat + 2, len(word)-1):
            #change this
            if [word[letters_repeat], word[letters_repeat + 1]] == [word[repetition], word[repetition+1]]:
                return True
    return False

def is_nice(word):
    return finding_nice_words_rule_1(word) and finding_nice_words_rule_2(word) and finding_nice_words_rule_3(word)     

def finding_nice_words(words):
    count = 0

    for word in words:
        if is_nice(word):
            count += 1

    return count



def finding_newer_nice_words(words):
    count = 0
    #fix like 1st star
    for word in words:
        first_rule_met = finding_newer_nice_words_rule_one(word)
        second_rule_met = finding_newer_nice_words_rule_two(word)
        
        if first_rule_met and second_rule_met:
            count += 1
    return count


print(finding_nice_words(all_words))
print(finding_newer_nice_words(all_words))

                        
