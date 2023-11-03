import re
from collections import Counter
import unittest
import day_1 as sut

instructions_recieved = 'R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3'
instructions_list = instructions_recieved.split(", ")

class Test_Day_1_Part_1(unittest.TestCase):
     
    def test_no_moves(self):
        instructions = []
        blocks = sut.part_1(instructions) 
        self.assertEqual(blocks, 0)

    def test_right_one_moves(self):
        instructions = ['R1']
        blocks = sut.part_1(instructions) 
        self.assertEqual(blocks, 1)

    def test_right_one_moves(self):
        instructions = ['L1']
        blocks = sut.part_1(instructions) 
        self.assertEqual(blocks, 1)

    def test_2_moves(self):
        instructions = ['R2', 'L3']
        blocks = sut.part_1(instructions) 
        self.assertEqual(blocks, 5)

    def test_3_moves(self):
        instructions = ['R2', 'R2', 'R2']
        blocks = sut.part_1(instructions) 
        self.assertEqual(blocks, 2)

    def test_4_moves(self):
        instructions = ['R5', 'L5', 'R5', 'R3']
        blocks = sut.part_1(instructions) 
        self.assertEqual(blocks, 12)

    def test_all_moves(self):
        blocks = sut.part_1(instructions_list) 
        self.assertEqual(blocks, 307)

class Test_Day_1_Part_2(unittest.TestCase):
    def test_no_moves(self):
        instructions = []
        blocks = sut.part_2(instructions) 
        self.assertEqual(blocks, None)


    def test_circles_back_to_start(self):
        instructions = ['R1', 'R1', 'R1', 'R1']
        blocks = sut.part_2(instructions) 
        self.assertEqual(blocks, 0)


#     def test_simplest_repetition(self):
#         instructions = ['R2', 'R1', 'R1', 'R10',]
#         blocks = sut.part_2(instructions) 
#         self.assertEqual(blocks, 1)
    
#     def test_simple_repetition(self):
#         instructions = ['L8', 'L4', 'L4', 'L8',]
#         blocks = sut.part_2(instructions) 
#         self.assertEqual(blocks, 4)

    

if __name__ == '__main__':
    unittest.main()