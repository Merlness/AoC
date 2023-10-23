def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

directions = list(fetch_test_data('../test_data/2016/day_2.txt'))

def decoder(code_list):
    x = -2
    y = 0
    buttons = []

    for move in code_list:
            coordinates = []

            for letter in move:
                a = x
                b = y
                if letter == 'U':
                    y += 1
                elif letter == 'D':
                    y -= 1
                elif letter == 'R':
                    x += 1
                elif letter == 'L':
                    x -= 1

                if (x,y) in [(-1,2), (1,2), (-2,1), (2,1), (-2,-1), (2,-1), (-1,-2), (1,-2), (0,3), (0,-3), (3,0), (-3,0)]:
                    x = a
                    y = b

            coordinates.append((x,y))
            for element in coordinates:
                if element == ( 0, 2):
                    buttons.append('1')
                if element == ( -1, 1):
                    buttons.append('2')
                if element == ( 0, 1):
                    buttons.append('3')
                if element == ( 1, 1):
                    buttons.append('4')
                if element == ( -2, 0):
                    buttons.append('5')
                if element == ( -1, 0):
                    buttons.append('6')
                if element == ( 0, 0):
                    buttons.append('7')
                if element == ( 1, 0):
                    buttons.append('8')
                if element == ( 2, 0):
                    buttons.append('9')
                if element == ( -1, -1):
                    buttons.append('A')
                if element == ( 0, -1):
                    buttons.append('B')
                if element == ( 1, -1):
                    buttons.append('C')
                if element == ( 0, -2):
                    buttons.append('D')

    print(buttons)


decoder(directions)