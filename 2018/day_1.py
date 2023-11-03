def part_1(frequencies):
    total = 0

    for frequency in frequencies:
        total = add_frequencies(frequency, total)

    return total

def add_frequencies(frequency, total):
    if frequency[0] == '-':
        total -= int(frequency[1:])
    else:
        total += int(frequency[1:])

    return total


def part_2(frequencies):
    total = 0
    possible_duplicates = [0]
    duplicate_not_found = True

    while duplicate_not_found:    
        for frequency in frequencies:
            total = add_frequencies(frequency, total)
            
            if is_duplicate(total, possible_duplicates):
                duplicate_not_found = False
                return total

            possible_duplicates.append(total)

    return total

def is_duplicate(total, possible_duplicates):
    if total in possible_duplicates:
        return True