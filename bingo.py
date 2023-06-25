import random as rm

class Bingocard:
    def __init__(self):
        self.hw = 5
        bingocard = [[None] * self.hw for _ in range(self.hw)]
        numbers = rm.sample([i for i in range(1, 75)], self.hw ** 2)
        for i in range(self.hw):
            if i == (self.hw - 1) / 2:
                for j in range(self.hw):
                    if j == (self.hw - 1) / 2:
                        bingocard[i][j] = 0
                    else:
                        bingocard[i][j] = numbers[i * self.hw + j]
            else:
                for j in range(self.hw):
                    bingocard[i][j] = numbers[i * self.hw + j]

        self.bingocard = bingocard

    def is_bingo(self):
        for i in range(self.hw):
            if self.bingocard[i][0] == self.bingocard[i][1] == self.bingocard[i][2] == self.bingocard[i][3] == self.bingocard[i][4] == 0:
                return True
        for j in range(self.hw):
            if self.bingocard[0][j] == self.bingocard[1][j] == self.bingocard[2][j] == self.bingocard[3][j] == self.bingocard[4][j] == 0:
                return True
        if self.bingocard[0][0] == self.bingocard[1][1] == self.bingocard[2][2] == self.bingocard[3][3] == self.bingocard[4][4] == 0:
            return True
        if self.bingocard[0][4] == self.bingocard[1][3] == self.bingocard[2][2] == self.bingocard[3][1] == self.bingocard[4][0] == 0:
            return True
        return False

    def punch(self, n):
        for i in range(self.hw):
            for j in range(self.hw):
                if n == self.bingocard[i][j]:
                    self.bingocard[i][j] = 0
                    break

def bingo():
    card = Bingocard()
    numbers = [i for i in range(1, 75)]
    rm.shuffle(numbers)
    x = 0
    for i in range(len(numbers)):
        card.punch(numbers[i])
        if card.is_bingo():
            x = i + 1
            break
    return x