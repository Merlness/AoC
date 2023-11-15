import unittest
import day_2_oo as sut
import re

final_opcode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]

class Test_Day_2_Part_1(unittest.TestCase):
    def test_first_program(self):
        opcode = [1,0,0,0,99]
        alarm = sut.part_1()
        alarm.get_program(opcode)
        program = alarm.fix_program() 
        self.assertEqual(program, [2,0,0,0,99])

    def test_second_program(self):
        opcode = [2,3,0,3,99]
        alarm = sut.part_1()
        alarm.get_program(opcode)
        program = alarm.fix_program() 
        self.assertEqual(program, [2,3,0,6,99])

    def test_third_program(self):
        opcode = [2,4,4,5,99,0]
        alarm = sut.part_1()
        alarm.get_program(opcode)
        program = alarm.fix_program() 
        self.assertEqual(program, [2,4,4,5,99,9801])

    def test_fourth_program(self):
        opcode = [1,1,1,4,99,5,6,0,99]
        alarm = sut.part_1()
        alarm.get_program(opcode)
        program = alarm.fix_program() 
        self.assertEqual(program, [30,1,1,4,2,5,6,0,99])

    def test_tough_program(self):
        opcode = [1,9,10,3,2,3,11,0,99,30,40,50]
        alarm = sut.part_1()
        alarm.get_program(opcode)
        program = alarm.fix_program() 
        self.assertEqual(program, [3500,9,10,70,2,3,11,0,99,30,40,50])

    def test_final_program(self):
        alarm = sut.part_1()
        alarm.get_program(final_opcode)
        program = alarm.fix_program() 
        self.assertEqual(program[0], 3267740)

class Test_Day_2_Part_2(unittest.TestCase):
    
    def test_final_program(self):
        alarm = sut.part_1()
        alarm.get_program(final_opcode)
        program = alarm.temp() 
        self.assertEqual(program, 19690720)



if __name__ == '__main__':
    unittest.main()

