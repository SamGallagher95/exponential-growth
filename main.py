from lib import app

numNodes = 1000
size = 300
travelRange = 5
infectionRate = .7
infectionChance = 1
initialInfected = 5
tickCount = 400
renderCount = 2
graphTitle = "Distancing Movement"

def main():
    run = app.App(numNodes, size, infectionRate, infectionChance, initialInfected, travelRange, tickCount, renderCount, graphTitle)

main()