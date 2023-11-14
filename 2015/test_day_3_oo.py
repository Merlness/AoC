import unittest
import day_3_oo as sut

import re
from collections import Counter

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

santa_directions = list(fetch_test_data('../test_data/2015/day_3.txt'))

class Test_Day_3_Part_1(unittest.TestCase):
    
    def test_no_move(self):
        direction = ['']
        santa = sut.Santa()
        houses = santa.get_houses(direction) 
        self.assertEqual(houses, 1)

    def test_1_move(self):
        direction = ['>']
        santa = sut.Santa()
        houses = santa.get_houses(direction) 
        self.assertEqual(houses, 2)
    
    def test_2_moves(self):
        direction = ['^', 'v']
        santa = sut.Santa()
        houses = santa.get_houses(direction)  
        self.assertEqual(houses, 2)

    def test_4_moves(self):
        direction = ['^', '>', 'v', '<']
        santa = sut.Santa()
        houses = santa.get_houses(direction)
        self.assertEqual(houses, 4)

    def test_all_moves(self):
        santa = sut.Santa()
        houses = santa.get_houses(santa_directions) 
        self.assertEqual(houses, 2592)

# class Test_Day_3_Part_2(unittest.TestCase):

#     def test_no_move(self):
#         direction = ['']
#         houses = sut.part_2(direction) 
#         self.assertEqual(houses, 1)

#     def test_1_move_each(self):
#         direction = ['^','v']
#         houses = sut.part_2(direction) 
#         self.assertEqual(houses, 3)

#     def test_3_moves_each(self):
#         direction = ['^', '>','v', '<']
#         houses = sut.part_2(direction) 
#         self.assertEqual(houses, 3)

#     def test_5_moves_each(self):
#         direction = ['^','v', '^', 'v', '^', 'v', '^', 'v', '^', 'v']
#         houses = sut.part_2(direction) 
#         self.assertEqual(houses, 11)
    
#     def test_all_moves(self):
#         houses = sut.part_2(santa_directions) 
#         self.assertEqual(houses, 2360)


if __name__ == '__main__':
    unittest.main()

