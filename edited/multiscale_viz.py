from plotly.subplots import make_subplots
import plotly.graph_objects as go

import plotly.express as px
import numpy

#box = numpy.random.normal( mean , stdev , (x_size, y_size))
boxes = []
# see surfaces.csv

# the flat cortex is 43x ~(7x7) larger than M1, which is 610x ~(25x25) larger than cortical column
# flat hemisphere + M1 + cortical column
# hemisphere
box = numpy.full((175, 175), 5)
# M1
box[:25, -25:] = numpy.full((25, 25), 4) # orientation [0][0] is bottom left
# cortical column
box[0][-1] = 3
boxes.append(box)

# cortical column contains 12800 ~(113x113) cells, which contain 66 ~(8x8) segments
# cortical column + cell + segment
# cortical
box = numpy.full((904, 904), 3)
# cell
box[:8:, -8:] = numpy.full((8, 8), 2)
# segment
box[0][-1] = 1
boxes.append(box)

# 1 cell contains 66 segments
# cell + segment
# cell
box = numpy.full((8, 8), 2)
# segment
box[0][-1] = 1
boxes.append(box)

# make plots
fig = make_subplots(1, len(boxes))
for i, box in enumerate(boxes):
    fig.add_trace(go.Heatmap(z=box, coloraxis="coloraxis"), 1, i+1)

fig.show()
