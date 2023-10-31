import unittest
import day_2 as sut

import re

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

def format_test_data(lines):
    return [int(s) for s in re.findall(r'\d+', lines)]

dimensions_list = [format_test_data(x) for x in fetch_test_data('../test_data/2015/day_2.txt')]


class Test_Day_2_Part_1(unittest.TestCase):

    def test_no_prism(self):
        dimension = [[0, 0, 0]]
        wrapping_paper = sut.part_1(dimension) 
        self.assertEqual(wrapping_paper, 0)

    def test_simplest_prism(self):
        dimension = [[1, 1, 1]]
        wrapping_paper = sut.part_1(dimension)
        self.assertEqual(wrapping_paper, 7)

    def test_simple_prism(self):
        dimension = [[2, 3, 4]]
        wrapping_paper = sut.part_1(dimension)
        self.assertEqual(wrapping_paper, 58)
    
    def test_medium_prism(self):
        dimension = [[1, 1 ,10]]
        wrapping_paper = sut.part_1(dimension)
        self.assertEqual(wrapping_paper, 43)
    
    def test_two_prisms(self):
        dimension = [[1, 1 ,10], [1, 1, 1]]
        wrapping_paper = sut.part_1(dimension)
        self.assertEqual(wrapping_paper, 50)

    def test_all_of_list(self):
        wrapping_paper = sut.part_1(dimensions_list)
        self.assertEqual(wrapping_paper, 1588178)

class Test_Day_2_Part_2(unittest.TestCase):

    def test_no_ribbon(self):
        dimension = [[0, 0, 0]]
        length_of_ribbon = sut.part_2(dimension) 
        self.assertEqual(length_of_ribbon, 0)

    def test_simplest_ribbon(self):
        dimension = [[1, 1, 1]]
        length_of_ribbon = sut.part_2(dimension) 
        self.assertEqual(length_of_ribbon, 5)

    def test_easy_ribbon(self):
        dimension = [[2, 3, 4]]
        length_of_ribbon = sut.part_2(dimension) 
        self.assertEqual(length_of_ribbon, 34)

    def test_medium_ribbon(self):
        dimension = [[1, 10, 1]]
        length_of_ribbon = sut.part_2(dimension) 
        self.assertEqual(length_of_ribbon, 14)
    
    def test_two_ribbons(self):
        dimension = [[1, 10, 1], [2, 3, 4]]
        length_of_ribbon = sut.part_2(dimension) 
        self.assertEqual(length_of_ribbon, 48)

    def test_all_of_list(self):
        length_of_ribbon = sut.part_2(dimensions_list) 
        self.assertEqual(length_of_ribbon, 3783758)

if __name__ == '__main__':
    unittest.main()

