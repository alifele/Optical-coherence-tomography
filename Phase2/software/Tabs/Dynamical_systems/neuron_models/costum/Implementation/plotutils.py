import numpy as np
import matplotlib.pyplot as plt
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.variables import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.functions import *

def arrow_plotter(v_range, w_range, I,ax, n=30):
    v_max = v_range[1]
    v_min = v_range[0]
    w_max = w_range[1]
    w_min = w_range[0]

    wRange = np.linspace(w_min, w_max, n)
    vRange = np.linspace(v_min, v_max, n)

    for i in range(n):
        for j in range(n):
            vd = v_dot(vRange[i], wRange[j], I)
            wd = w_dot(vRange[i], wRange[j])
            norm = (vd**2 + wd**2)**0.5 * 6
            #norm = 50
            ax.arrow(wRange[j], vRange[i], wd/norm, vd/norm, head_width=0.05)
            #plt.arrow( vRange[i], wRange[j], wd/norm, vd/norm, head_width=0.1)


def eigplot(jacob):
    W,V = np.linalg.eig(jacob)
    #V = np.real(V)
    print('W = {}'.format(W))
    print('V = {}'.format(V))
    x1 = np.linspace(w_range[0], w_range[1],10)
    for i in range(len(W)):
        if V[0,i] == 0:
            plt.axvline(0)
        else:
            y = V[1,i]/V[0,i] * x1
            plt.plot(x1,y, 'r--', label='eigen', alpha=1)





def ANIMATIO():
    pass
