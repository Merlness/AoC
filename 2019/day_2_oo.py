import copy

class part_1:
    def __init__(self):
        self.program = []
        self.copy_of_program = []
        

    def get_program(self, opcode):
        self.program = opcode
        self.copy_of_program = copy.deepcopy(opcode)

    def fix_program(self):
        code = self.program
       
        for fourth in range(0, len(code), 4):
            if code[fourth] in [1,2]:
                code[code[fourth + 3]] = self.add_or_mult(code, fourth)
            elif code[fourth] == 99:
                break

        return code

    def change_code(self, code, fourth, sign):
        if sign == '+':
            return code[code[fourth + 1]] + code[code[fourth + 2]]
        return code[code[fourth + 1]] * code[code[fourth + 2]]
    
    def add_or_mult(self, code, fourth):
        if code[fourth] == 1:
            return self.change_code(code,fourth, '+')              
        elif code[fourth] == 2:
            return self.change_code(code,fourth, '*')

    def fix_part_2(self, noun, verb):
        self.copy_of_program = self.copy_of_program.copy()
        self.program[1] = noun
        self.program[2] = verb
        self.fix_program()

    def temp(self):
        for noun in range(100):
            for verb in range(100):
                self.fix_part_2(noun, verb)
                print(self.program[0])
                if self.program[0] == 19690720:
                    return 100 * noun + verb    


# class part_2:
#     def __init__(self):
#         self.program = []
#         self.copy_of_program = []
        

#     def get_program(self, opcode):
#         self.program = opcode
#         self.copy_of_program = copy.deepcopy(opcode)

    # def fix_part_2(self, noun, verb):
    #     self.program = self.copy_of_program.copy()
    #     self.program[1] = noun
    #     self.program[2] = verb
    #     part_1.fix_program(self)

    # def temp(self):
    #     for noun in range(100):
    #         for verb in range(100):
    #             self.fix_part_2(noun, verb)
    #             print(self.program[0])
    #             if self.program[0] == 19690720:
    #                 return 100 * noun + verb    

#def dummy(self):
#   program = self.program
#   for noun in range(100):
#     for verb in range(100):
        #   program[1] = noun
        #   program[2] = verb
#           fix program()
#           if program[0] == 19690720:
            #   return 100 * noun + verb
#           else:
#               self.program = self.copy_of_program    
#                dummy