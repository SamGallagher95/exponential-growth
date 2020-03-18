# Exponential Growth Simulation

Read the article here: https://medium.com/@gallaghersam95/exponential-growth-e064cc3a54ea

## Dependencies

Reqires `matplotlib` and `pandas`.

## Usage

The entrypoint is the file `main.py`, it contains all of the values that can be tweaked in the simulation. It will output simulation frames to both the `Growth` and `nodeMap` directories inside of the project. If those directories do not exist before running the simulation, it will fail.

### Random Movement

To enable Random Movement, be sure that lines 65 and 66 in `lib/app.py` are commented out. Here are those lines for reference:

```
nodes = self.nearbyNodes(node)
node.newSocialDistancingPositioning(nodes, maxRange=self.travelRange)
```

AND be sure that line 67 in `lib/app.py` is uncommented. Here is that line for reference:

```
node.newPosition(maxRange=self.travelRange)
```

### Distancing Movement

To enable Distancing Movement, follow the instructions opposite to Random Movement. So lines 65 and 66 are uncommented, and 67 is commented out in `lib/app.py`.