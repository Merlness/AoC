import re
#part 1
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

#part 2
def ribbon_feet(dimension):
    short_side_1 = sorted(dimension)[0]
    short_side_2 = sorted(dimension)[1]

    return ( 2 * short_side_1
            + 2 * short_side_2
            + (dimension[0]
            * dimension[1]
            * dimension[2]))

def ribbon_total(data):
    ribbon_total = 0

    ribbon = [ribbon_feet(dimension) for dimension in data]
    ribbon_total = sum(ribbon)

    return print(ribbon_total)

wrapping_paper(dimensions_list)
ribbon_total(dimensions_list)
print(dimensions_list)