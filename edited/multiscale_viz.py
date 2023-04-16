import plotly.express as px
import numpy

#box = numpy.random.normal( mean , stdev , (x_size, y_size))

#total cortical grey matter    (814)
#total subcortical grey matter  (54)
#total white matter            (601)
#==================================
#total                        (1469)

#length?
#this box represents the system (10^3)
box0 = numpy.full((32, 32), 5)

#fill area (10^2) of system (10^3)
box0[-10:, -10:] = numpy.full((10, 10), 4)

#fill local circuit (10^1.1)
box0[-4:,-4:] = numpy.full((4, 4), 3)

#fill column (10^0.1)
box0[-1][-1] = 2

#fill layer (10^-0.6)

#fill cell (10^-0.7)

#fill dendrite (10^-0.9)
fig = px.imshow(box0)

fig.show()