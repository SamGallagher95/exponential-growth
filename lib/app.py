from .node import Node
import json
import random
import math
import pandas
import progressbar
import matplotlib.pyplot as plt

class App():
    def __init__(self, numNodes, size, infectionRate, infectionChance, initialInfected, travelRange, tickCount):
        self.tick = 0
        self.infected = []

        self.numNodes = numNodes
        self.size = size
        self.infectionRate = infectionRate
        self.infectionChance = infectionChance
        self.travelRange = travelRange

        self.initNodes()
        self.printNodeMap()

        for i in range(initialInfected):
            self.infectRandomNode()

        bar = progressbar.ProgressBar(maxval=tickCount,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()

        count = 0
        while (True):
            bar.update(count)
            flag = self.tickFunc()
            count += 1

            # Check if we need to redraw the nodeMap
            if count % 100 == 0:
                self.printNodeMap()

            # Check the status of the count
            if flag is True or count > tickCount:
                self.finish()
                bar.finish()
                break

    def initNodes(self):
        self.nodes = []
        for i in range(self.numNodes):
            self.nodes.append(Node(self.size))
    
    def infectRandomNode(self):
        x = random.randint(0,len(self.nodes) - 1)
        node = self.nodes[x]
        node.infect()

    def tickFunc(self):
        self.tick += 1

        infectedCount = 0
        for node in self.nodes:
            node.newPosition(maxRange=self.travelRange)
            if node.infected is False:
                if self.chanceInfection(node) is True:
                    node.infect()
                    infectedCount += 1
            else:
                infectedCount += 1

        self.tick += 1
        self.infected.append(infectedCount)
        
        return self.checkNodes()

    def chanceInfection(self, targetNode):
        flag = False
        for node in self.nodes:
            if node.infected is True:
                (x_d, y_d) = (node.x - targetNode.x, node.y - targetNode.y)
                x = math.sqrt((math.pow(x_d, 2)) + (math.pow(y_d, 2)))
                x_n = self.sigmoid(x)
                if x_n <= self.infectionRate:
                    flag = True
        return flag

    def checkNodes(self):
        flag = True
        for node in self.nodes:
            if node.infected is False:
                flag = False
        return flag

    def sigmoid(self, x):
        return 1 / (1 + (math.pow(math.e, x*-1 + self.infectionChance)))

    def finish(self):
        self.printInfectedGraph()
        self.printInfectedGrowth()

    def printNodeMap(self):
        fig, ax = plt.subplots(nrows=1, ncols=1)
        for node in self.nodes:
            color = "green"
            if node.infected is True:
                color = "red"
            ax.plot(node.x, node.y, "o", color=color)
        fig.savefig("nodeMap.png")
        plt.close(fig)
    
    def printInfectedGraph(self):
        df = pandas.DataFrame(self.infected)
        fig, ax = plt.subplots(nrows=1, ncols=1)
        ax.plot(df)
        fig.savefig("infected.png")
        plt.close(fig)
    
    def printInfectedGrowth(self):
        growth = []
        for index, i in enumerate(self.infected[1:]):
            growth.append(i / self.infected[index - 1])
        df = pandas.DataFrame(growth[1:])
        fig, ax = plt.subplots(nrows=1, ncols=1)
        ax.plot(df)
        fig.savefig("growth.png")
        plt.close(fig)

    def printNodes(self):
        for node in self.nodes:
            print(f"Node: x: {node.x} y: {node.y} infected: {node.infected}")