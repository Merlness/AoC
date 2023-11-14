class elves:
    
    def __init__(self):
        self.wrapping_paper = 0
        self.ribbon_length = 0

        self.length = 0
        self.width = 0
        self.height = 0
        self.wrapping_paper = 0
# try to have your getters do little work - readonly
# while setters do all the work - write
# put for loop of calc wrap and ribbon in wrap


    def get_wrapping_paper(self):
        return self.wrapping_paper
    
    def get_ribbon_length(self):
        return self.ribbon_length
    
    def wrap(self, gifts):
        # do work...
        self.ribbon_length = self.calc_ribbon(gifts)
        self.wrapping_paper = self.calc_wrapping_paper(gifts)

    
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
