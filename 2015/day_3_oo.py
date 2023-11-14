class Santa:
    def __init__(self):
        self.houses = 1
        self.x = 0
        self.y = 0
        self.coordinates = {(0, 0)}
    
    def get_houses(self, moves):
        X = self.x
        Y = self.y

        for move in moves:
            X, Y = self.track_santa(move, X, Y)
            self.coordinates.add((X, Y))
            houses = len(self.coordinates)

        return houses

    def track_santa(self, move, x, y):
        if move == '>':
            x += 1
        elif move == '^':
            y += 1
        elif move == '<':
            x -= 1
        elif move == 'v':
            y -= 1

        return x, y
        