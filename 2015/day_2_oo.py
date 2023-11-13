class elves:
    
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
        self.wrapping_paper = 0

    
    def calc_wrapping_paper(self, dimensions):
        wrapping_paper = self.wrapping_paper

        for dimension in dimensions:
            wrapping_paper += self.find_wrapping_paper(dimension)

        return wrapping_paper
    
    def find_surface_area(self, dimension):
        [self.length, self.width, self.height] = dimension

        area = [self.length * self.width, 
                 self.length * self.height, 
                 self.height * self.width]
       
        return area

    def find_wrapping_paper(self, dimension):
        surface_area = self.find_surface_area(dimension)
        area = 2 * sum(surface_area)
        extra_paper = min(surface_area)
        wrapping_paper = area + extra_paper
        
        return wrapping_paper
        
    def calc_ribbon(self, dimensions):
        ribbon = 0

        for dimension in dimensions:
            wrap = 2 * (sum(dimension) - max(dimension))
            bow = self.find_bow(dimension)

            ribbon += wrap + bow

        return ribbon
    
    def find_bow(self, dimension):
        [self.length, self.width, self.height] = dimension
        bow = self.length * self.width * self.height

        return bow
