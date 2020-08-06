import numpy as np

w = -2
v = 0
I = 0
t_total = 600
dt = 0.05
t = np.arange(0,t_total, dt)
w_range = [-5, 5]
v_range = [-5, 5]
jacob = np.array([[1,-1],[0.08, -0.8*0.08]])


# [[1-3v^2, -1],[0.08, -0.8*0.08]] --> jakobian matrix
#
#
#
