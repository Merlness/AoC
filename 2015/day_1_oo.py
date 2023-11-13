class Santa:
    def __init__(self):
        self.floor = 0
        self.has_entered_basement = False
        self.number_of_moves = 0
    
    def get_floor(self, moves):
        for move in moves:
            self.floor += self.decode_move(move)
        return self.floor
    
    def decode_move(self,move):
        if move == '(':
            return 1
        elif move == ')':
            return - 1
        

    def check_basement(self, moves):
        for move in moves:
            self.number_of_moves += 1
                
            self.floor += self.decode_move(move)
            
            if self.is_in_basement():
                return self.number_of_moves

    def is_in_basement(self):
        if self.floor == -1:
            return True
         
