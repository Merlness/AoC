import re

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

def format_test_data(lines):
    return [int(s) for s in re.findall(r'\d+', lines)]

dimensions_list = [format_test_data(x) for x in fetch_test_data('../test_data/2015/day_2.txt')]

def area(dimension):
    length = dimension[0]
    width = dimension[1]
    height = dimension[2]
    
    return (2 * length * width 
            + 2 * width * height 
            + 2 * length * height 
            + min(length * width, width * height, length * height))

def wrapping_paper(data):
    total_wrapping_paper=0

    feet_of_wrapping_paper = [area(dimension) for dimension in data]
    total_wrapping_paper = sum(feet_of_wrapping_paper)

    return print(total_wrapping_paper)

wrapping_paper(dimensions_list)