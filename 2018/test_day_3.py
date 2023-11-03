import unittest
import day_3 as sut

def fetch_test_data(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text.split("\n")

rectangle_claims = list(fetch_test_data('../test_data/2018/day_3.txt'))

class Test_Day_2_Part_1(unittest.TestCase):
     
    def test_no_rectangle(self):
        claim = []
        overlap = sut.part_1(claim) 
        self.assertEqual(overlap, 0)

    def test_no_rectangle(self):
        claim = []
        overlap = sut.part_1(claim) 
        self.assertEqual(overlap, 0)


if __name__ == '__main__':
    unittest.main()