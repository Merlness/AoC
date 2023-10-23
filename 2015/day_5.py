import re

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

all_words = list(fetch_test_data('../test_data/2015/day_5.txt'))

def word_shifter(words):
    count = 0

    for word in words:
        one = True
        two = False
        three = False

        for pair in ['xy','ab','cd','pq']:
            if word.find(pair) >= 0:
                one = False
        # Leaving this code below here because RegEx is tough
        #   if re.findall('xy'or'ab'or 'cd' or 'pq',i) == []:
        #       one = True

        if len(re.findall(r'a|e|i|o|u', word)) > 2:
            two = True

        for c in range(len(word)):
            if word[c] == word[c-1] and c!= 0:
                three = True

        if one and two and three:
            count += 1
            
    print(count)

def new_nice_words(words):
    count = 0

    for word in words:
        one = False
        two = False

        for letter_repeats in range(len(word)):
            if word[letter_repeats] == word[letter_repeats -2] and letter_repeats > 1:
                one = True
        
        for letters_repeat in range(len(word)):
            for repetition in range(letters_repeat + 2, len(word)-1):
                if [word[letters_repeat], word[letters_repeat + 1]] == [word[repetition], word[repetition+1]]:
                    two = True

        if one and two:
            count += 1
    print(count)


word_shifter(all_words)
new_nice_words(all_words)

                        
