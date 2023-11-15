#no health benfits, 

class fuel_requirement:
    def __init__(self):
        self.fuel = 0
        self.divisor = 3
        self.extra_fuel = 0

    def find_fuel(self):
        return self.fuel
    
    def find_true_fuel(self):
        return self.extra_fuel
    
    def recieve_mass(self, mass):
        self.fuel = self.calc_fuel(mass)
        self.extra_fuel = self.part_2(mass)

    def calc_fuel(self, masses):
        return self.sum_by(masses, self.calculation)

    def calculation(self, mass):
        divisor = self.divisor
        return max(0, int((mass - (mass % divisor))/divisor) - 2)
        
    def part_2(self, masses):
        return self.sum_by(masses, self.calc_extra_fuel)

    def calc_extra_fuel(self, mass):
        fuel = 0
        
        add_fuel = self.calculation(mass)
        fuel += add_fuel
        if add_fuel > 0:
            fuel += self.calc_extra_fuel(add_fuel)

        return fuel
    
    def sum_by(self, collection, measure):
        total = 0
        
        for item in collection:
            total += measure(item)

        return total