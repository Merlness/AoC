import unittest
import day_2 as sut

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

box_of_IDs = list(fetch_test_data('../test_data/2018/day_2.txt'))


class Test_Day_2_Part_1(unittest.TestCase):
     
    def test_no_letters(self):
        box_IDs = []
        checksum = sut.part_1(box_IDs) 
        self.assertEqual(checksum, 0)

    def test_no_duplicates(self):
        box_IDs = ['abcdef']
        checksum = sut.part_1(box_IDs) 
        self.assertEqual(checksum, 0)
    
    def test_simplest_duplicate(self):
        box_IDs = ['aa']
        checksum = sut.part_1(box_IDs) 
        self.assertEqual(checksum, 0)

    def test_simplest_ID(self):
        box_IDs = ['bababc']
        checksum = sut.part_1(box_IDs) 
        self.assertEqual(checksum, 1)
    
    def test_simple_two_IDs(self):
        box_IDs = ['bababc', 'abbcde']
        checksum = sut.part_1(box_IDs) 
        self.assertEqual(checksum, 2)

    def test_AoC_test(self):
        box_IDs = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
        checksum = sut.part_1(box_IDs) 
        self.assertEqual(checksum, 12)
    
    def test_whole_list(self):
        checksum = sut.part_1(box_of_IDs) 
        self.assertEqual(checksum, 12)

class Test_Day_2_Part_1(unittest.TestCase):

    def test_two_ids(self):
        box_IDs = ['aa', 'ab']
        checksum = sut.part_2(box_IDs) 
        self.assertEqual(checksum, 'a')
     
    def test_AoC_test(self):
        box_IDs = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
        checksum = sut.part_2(box_IDs) 
        print(checksum)
        self.assertEqual(checksum, 'fgij')

    def test_whole_list(self):
        checksum = sut.part_2(box_of_IDs) 
        self.assertEqual(checksum, 'jbbenqtlaxhivmwyscjukztdp')


if __name__ == '__main__':
    unittest.main()