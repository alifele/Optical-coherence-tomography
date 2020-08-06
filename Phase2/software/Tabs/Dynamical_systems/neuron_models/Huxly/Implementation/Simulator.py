import numpy as np
import matplotlib.pyplot as plt
from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.Simulator_functions import *
import Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.variables as var
from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.animutils import Animationcls
from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.animation_run import run_animation

v = -63
n = 0
m = 0
h = 0
dt = 0.001
t_total = 10
t = np.arange(0, t_total, dt)
I = 1 # nAmp
#I_list = [3*i for i in range(1,100)]
I_list = [20]
spikes_list = []

for I in I_list:
    v_list, n_list, m_list, h_list, N_spikes = experiment_run(v,n,m,h,I,t_total, dt)

    spikes_list.append([I, N_spikes])

run_animation(v_list, n_list, m_list, h_list, N_spikes,I,t)
