import random
import math
from functools import reduce

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
        x_r = random.random() * self.maxRange
        y_r = random.random() * self.maxRange
        
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
        
    def newSocialDistancingPositioning(self, nodes, maxRange=0):
        angles = [0]
        for node in nodes:
            if node.x == self.x and node.y == self.y:
                continue
            elif node.y == self.y:
                angles.append(0)
            else:
                if node.x > self.x:
                    x = node.x - self.x
                else:
                    x = self.x - node.x
                if node.y > self.x:
                    y = node.y - self.y
                else:
                    y = self.y - node.y
                angles.append(math.sin(x / y))
        
        avg = reduce(lambda a, x: a + x, angles) / len(angles)
        avg *= math.pi * -1

        m = (random.random() * maxRange) * self.getSign()

        x = m * math.sin(avg)
        y = m * math.cos(avg)
        self.x += x
        self.y += y
    
    def getSign(self):
        x = random.random()
        if x > .5:
            return 1
        else:
            return -1