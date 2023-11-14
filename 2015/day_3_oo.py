class Santa:
    # try to have your getters do little work - readonly
    # while setters do all the work - write
    # put for loop of calc wrap and ribbon in wrap

    def __init__(self):
        self.houses = 1
        self.x = 0
        self.y = 0
        self.a = 0
        self.b = 0
        self.coordinates = {(0, 0)}
        self.robo_coordinates = {(0, 0)}
        self.houses = 0
        self.robo_santa_houses = 0
        self.santas_turn = True
        
    
    def get_houses(self):
        return self.houses
    
    def get_robo_and_santa_houses(self):
        return self.robo_santa_houses

    def recieve_message(self, message):
        self.houses = self.decode_message(message)
        self.robo_santa_houses = self.decode_robo_and_santa(message)

    def decode_message(self, moves):
        X = self.x
        Y = self.y

        for move in moves:
            X, Y = self.track_santa(move, X, Y)
            self.coordinates.add((X, Y))

        return len(self.coordinates)

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
    
    def decode_robo_and_santa(self, moves):
        X = self.x
        Y = self.y
        A = self.a
        B = self.b

        for move in moves:
            if self.santas_turn:
                X, Y = self.track_santa(move, X, Y)
                self.robo_coordinates.add((X, Y))
            else:
                A, B = self.track_santa(move, A, B)
                self.robo_coordinates.add((A, B))

            self.santas_turn = not self.santas_turn
        
        return len(self.robo_coordinates)



    
        