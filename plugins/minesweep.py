import random

class Minesweeper:
    NULL = 0
    MINE = 9
    BOOM = 10
    OPENED = True
    UNOPENED = False

    def __init__(self, size = 4, mineraito = 0.2):
        self.init_stage(size, mineraito)

    def init_stage(self, size, mineraito):
        self.size = size
        self.mineraito = mineraito
        self.stage = [[self.NULL if random.random() > mineraito else self.MINE \
                     for i in range(self.size)]
                     for j in range(self.size)]
        self.state = [[self.UNOPENED \
                     for i in range(self.size)]
                     for j in range(self.size)]
        self.stage = [[self.neighborcell(i, j)
                     for i in range(self.size)]
                     for j in range(self.size)]

    def neighborcell(self, row, col):
        if self.stage[row][col] == self.MINE :
            return self.MINE

        neighbor = self.NULL
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif -1 < (row + i) < self.size and -1 < (col + j) < self.size:
                    if self.stage[row+i][col+j] == self.MINE:
                        neighbor = neighbor + 1
        return neighbor

    def sweep(self, row , col):
        if self.state[row][col] == self.UNOPENED :
            self.state[row][col] = self.OPENED
            if self.stage[row][col] == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if -1 < (row + i) < self.size and -1 < (col + j) < self.size:
                            self.sweep(row+i, col+j)
            return self.stage[row][col] != self.MINE

    def fullopen(self, row, col):
        self.state = [[self.OPENED \
                     for i in range(self.size)]
                     for j in range(self.size)]
        self.stage[row][col] = self.BOOM

    def shaping(self, instr):
        comstr = instr.replace(" ","")
        row, col = comstr.split(",")
        return int(row), int(col)

    def generate_message(self):
        mess = ""
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == self.UNOPENED :
                    mess = mess + ":white_square_button:"
                else:
                    if self.stage[i][j] == 0:
                        mess = mess + ":white_square:"
                    if self.stage[i][j] == 1:
                        mess = mess + ":one:"
                    if self.stage[i][j] == 2:
                        mess = mess + ":two:"
                    if self.stage[i][j] == 3:
                        mess = mess + ":three:"
                    if self.stage[i][j] == 4:
                        mess = mess + ":four:"
                    if self.stage[i][j] == 5:
                        mess = mess + ":five:"
                    if self.stage[i][j] == 6:
                        mess = mess + ":six:"
                    if self.stage[i][j] == 7:
                        mess = mess + ":seven:"
                    if self.stage[i][j] == 8:
                        mess = mess + ":eight:"
                    if self.stage[i][j] == 9:
                        mess = mess + ":bomb:"
                    if self.stage[i][j] == 10:
                        mess = mess + ":boom:"
            mess = mess + "\n"
        return mess

    def show_debug(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == self.UNOPENED :
                    print("X",end="")
                else:
                    print(self.stage[i][j], end="")
            print("\n" ,end="")  

"""

ms = Minesweeper(7, 0.1)
while 1:
  ms.show_debug()
  inkey = input()
  row, col =  ms.shaping(inkey)
  if ms.sweep(row, col) == False :
      ms.fullopen(row, col)
      ms.show_debug()
      ms = Minesweeper(7, 0.1)
"""      
