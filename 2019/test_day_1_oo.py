import unittest
import day_1_oo as sut
import re

def fetch_test_data(path):
    with open(path, "r") as file:
        text = file.read()
    return text.split("\n")

def format_test_data(lines):
    return [int(s) for line in lines for s in re.findall(r'\d+', line)]

mass_list = format_test_data(fetch_test_data('../test_data/2019/day_1.txt'))

class Test_Day_1_Part_1(unittest.TestCase):
    def test_first_mass(self):
        mass = [12]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 2)

    def test_second_mass(self):
        mass = [14]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 2)

    def test_third_mass(self):
        mass = [1969]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 654)

    def test_fourth_mass(self):
        mass = [100756]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 33583)

    def test_two_masses(self):
        mass = [12, 14]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 4)

    def test_three_masses(self):
        mass = [12, 14, 1969]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 658)

    def test_multiple_masses(self):
        mass = [12, 14, 1969, 100756]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 34241)

    def test_final(self):
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass_list)
        fuel = santa.find_fuel() 
        self.assertEqual(fuel, 3497998)


class Test_Day_1_Part_2(unittest.TestCase):
    def test_first_mass(self):
        mass = [12]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_true_fuel() 
        self.assertEqual(fuel, 2)

    def test_second_mass(self):
        mass = [1969]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_true_fuel() 
        self.assertEqual(fuel, 966)

    def test_third_mass(self):
        mass = [100756]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_true_fuel() 
        self.assertEqual(fuel, 50346)

    def test_two_masses(self):
        mass = [100756, 1969]
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass)
        fuel = santa.find_true_fuel() 
        self.assertEqual(fuel, 51312)

    def test_final(self):
        santa = sut.fuel_requirement()
        santa.recieve_mass(mass_list)
        fuel = santa.find_true_fuel() 
        self.assertEqual(fuel, 5244112)

    

if __name__ == '__main__':
    unittest.main()

