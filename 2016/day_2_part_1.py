def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

directions = list(fetch_test_data('../test_data/2016/day_2.txt'))

def decoder(code):
    x = 0
    y = 0
    numbers = []

    for move in code:
            coordinates = []

            for letter in move:
                if letter == 'U':
                    y += 1
                elif letter == 'D':
                    y -= 1
                elif letter == 'R':
                    x += 1
                elif letter == 'L':
                    x -= 1

                if x == 2:
                    x = 1
                if x == -2:
                    x = -1
                if y == 2:
                    y = 1
                if y == -2:
                    y = -1

            coordinates.append((x,y))
            for element in coordinates:
                if element == ( -1, 1):
                    numbers.append('1')
                if element == ( 0, 1):
                    numbers.append('2')
                if element == ( 1, 1):
                    numbers.append('3')
                if element == ( -1, 0):
                    numbers.append('4')
                if element == ( 0, 0):
                    numbers.append('5')
                if element == ( 1, 0):
                    numbers.append('6')
                if element == ( -1, -1):
                    numbers.append('7')
                if element == ( 0, -1):
                    numbers.append('8')
                if element == ( 1, -1):
                    numbers.append('9')

    print(numbers)


decoder(directions)

