import numpy as np
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.variables import *


def w_dot(v,w):
    return 0.08*(v + 0.7 - 0.8*w)

def v_dot(v,w,I):
    return v - v**3 - w + I


def var_updater(var, var_dot, dt):
    var += var_dot * dt
    return var


def run_experiment(v,w,I,t_total, dt):
    v_list = []
    w_list = []
    v_dot_list = []
    w_dot_list = []
    for _ in range(int(t_total/dt)):

        vd = v_dot(v,w,I)
        wd = w_dot(v,w)
        v = var_updater(v, vd, dt)
        w = var_updater(w, wd, dt)
        v_list.append(v)
        w_list.append(w)
        v_dot_list.append(vd)
        w_dot_list.append(wd)


    return v_list, w_list, v_dot_list, w_dot_list
