from lib import app

numNodes = 1000
size = 100
travelRange = 5
infectionRate = .3
infectionChance = 1
initialInfected = 5
tickCount = 500

def main():
    run = app.App(numNodes, size, infectionRate, infectionChance, initialInfected, travelRange, tickCount)

main()