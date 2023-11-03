import unittest
import day_1 as sut

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

text_of_changes = list(fetch_test_data('../test_data/2018/day_1.txt'))


class Test_Day_1_Part_1(unittest.TestCase):
     
    def test_no_change(self):
        frequency_changes = []
        frequency = sut.part_1(frequency_changes) 
        self.assertEqual(frequency, 0)

    def test_1_change(self):
        frequency_changes = ['+1']
        frequency = sut.part_1(frequency_changes) 
        self.assertEqual(frequency, 1)

    def test_2_changes(self):
        frequency_changes = ['+1', '-2']
        frequency = sut.part_1(frequency_changes) 
        self.assertEqual(frequency, -1)

    def test_3_changes(self):
        frequency_changes = ['+1', '+1', '+1']
        frequency = sut.part_1(frequency_changes) 
        self.assertEqual(frequency, 3)    
     
    def test_3_harder_changes(self):
        frequency_changes = ['-1', '-2', '-3']
        frequency = sut.part_1(frequency_changes) 
        self.assertEqual(frequency, -6) 
    
    def test_full_list(self):
        frequency = sut.part_1(text_of_changes) 
        self.assertEqual(frequency, 533) 

class Test_Day_1_Part_2(unittest.TestCase):
     
    # def test_no_change(self):
    #     frequency_changes = []
    #     frequency_repetition = sut.part_2(frequency_changes) 
    #     self.assertEqual(frequency_repetition, None)

    def test_2_changes(self):
        frequency_changes = ['+1', '-1']
        frequency_repetition = sut.part_2(frequency_changes) 
        self.assertEqual(frequency_repetition, 0)

    def test_3_changes(self):
        frequency_changes = ['+2', '-1', '+1']
        frequency_repetition = sut.part_2(frequency_changes) 
        self.assertEqual(frequency_repetition, 2)
    
    def test_5_changes(self):
        frequency_changes = ['+10', '-5', '+1', '+3', '-4']
        frequency_repetition = sut.part_2(frequency_changes) 
        self.assertEqual(frequency_repetition, 5)

    def test_first_recursion(self):
        frequency_changes = ['+3', '+3', '+4', '-2', '-4']
        frequency_repetition = sut.part_2(frequency_changes) 
        self.assertEqual(frequency_repetition, 10)

    def test_second_recursion(self):
        frequency_changes = ['-6', '+3', '+8', '+5', '-6']
        frequency_repetition = sut.part_2(frequency_changes) 
        self.assertEqual(frequency_repetition, 5) 

    def test_third_recursion(self):
        frequency_changes = ['+7', '+7', '-2', '-7', '-4']
        frequency_repetition = sut.part_2(frequency_changes) 
        self.assertEqual(frequency_repetition, 14)

    # def test_final_recursion(self):
    #     frequency_repetition = sut.part_2(text_of_changes) 
    #     self.assertEqual(frequency_repetition, 73272)

if __name__ == '__main__':
    unittest.main()