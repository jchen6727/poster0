import plotly.express as px
import numpy

#box = numpy.random.normal( mean , stdev , (x_size, y_size))

# see surfaces.csv
# the flat cortex is 43x ~(7x7) larger than M1, which is 610x ~(25x25) larger than cortical column

# flat hemisphere + M1 + cortical column

# hemisphere
box0 = numpy.full((175, 175), 5)

# M1
box0[-25:, -25:] = numpy.full((25, 25), 4)

# cortical column
box0[-1][-1] = 3

# show
#fig = px.imshow(box0, zmin = 1, zmax = 3)

# cortical column
box1 = numpy.full((904, 904), 3)

# cell
box1[-8:, -8:] = numpy.full((8, 8), 2)

# segment
box1[-1][-1] = 1

# show
fig = px.imshow(box1, zmin = 1, zmax = 3)
fig.show()