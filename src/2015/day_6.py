import numpy as np

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

text = list(fetch_test_data('../test_data/2015/day_6.txt'))
grid = np.zeros((1000,1000))

test_grid = np.zeros((10,10))

test  = ['turn on 4,8 through 7,9' ,'turn off 7,5 through 8,9' ,'turn off 4,0 through 9,2', 'toggle 2,6 through 3,7']


def light_control(directions):
    formatted_test = []
    on =0
    off = 0
    toggle = 0

    for string in range(len(directions)):
        # print(string)
        formatted_test.append(directions[string].split())

        if any('on' in sublist for sublist in formatted_test):    
            #grid[3:7, 3:7] = 1
            on += 1 
        elif any('off' in sublist for sublist in formatted_test):
            #grid[3:7, 3:7] = 0
            off += 1
        elif any('toggle' in sublist for sublist in formatted_test):
            #grid[3:7, 3:7] = 1 - grid[3:7, 3:7]
            toggle +=1
            
    print(on, off, toggle)
    return formatted_test


in_grid = np.ones((2,2))


# print(test)
light_control(test)
# print(test[0].split())














# grid[4:6,4:6] = in_grid


# print(grid)


# Toggle 
# grid[3:7, 3:7] = 1 - grid[3:7, 3:7]
# grid[3:7, 3:7] = True
# grid[3:7, 3:7] = not grid[3:7, 3:7]

# print(grid)