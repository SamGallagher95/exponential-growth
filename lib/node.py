import random

class Node():
    def __init__(self, size):
        self.maxRange = size

        self.x = 0
        self.y = 0
        self.newPosition(start=True)

        self.infected = False
    
    def infect(self):
        self.infected = True

    def newPosition(self, maxRange=0, start=False):
        x_r = random.randint(0, self.maxRange)
        y_r = random.randint(0, self.maxRange)
        
        if start:
            self.x = x_r % self.maxRange
            self.y = y_r % self.maxRange
            return
        else:
            x_r %= maxRange
            if x_r >= self.maxRange:
                x_r -= self.maxRange
            elif x_r < 0:
                x_r += self.maxRange
            
            y_r %= maxRange
            if y_r >= self.maxRange:
                y_r -= self.maxRange
            elif y_r < 0:
                y_r += self.maxRange

            self.x = self.x + ((x_r % maxRange) * self.getSign())
            self.y = self.y + ((y_r % maxRange) * self.getSign())
    
    def getSign(self):
        x = random.random()
        if x > .5:
            return 1
        else:
            return -1