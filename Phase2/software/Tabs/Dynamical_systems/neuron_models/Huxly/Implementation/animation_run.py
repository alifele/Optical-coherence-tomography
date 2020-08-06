import numpy as np
import matplotlib.pyplot as plt
from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.Simulator_functions import *
import Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.variables as var
from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.animutils import Animationcls


def run_animation(v_list, n_list, m_list, h_list, N_spikes,I,t):


    fig = plt.figure()
    #ax = fig.add_subplot(4,4,(1,16))
    #ax.set_yticks([])
    #ax.axis('off')

    ax = fig.add_subplot(6,4,(1,4), title = 'I = {} $nAmp$'.format(I))
    ax.plot(t, v_list,'--',alpha=0.5, label='v_list')
    ax.set_xticks([])
    ax.set_ylabel('V')
    line1, = ax.plot([],[],lw=3)


    ax = fig.add_subplot(6,4,(5,8))
    ax.plot(t, n_list,'--',alpha=0.5, label='n_list')
    ax.set_xticks([])
    ax.set_ylabel('n')
    line2, = ax.plot([],[],lw=3)

    ax = fig.add_subplot(6,4,(9,12))
    ax.plot(t, h_list,'--',alpha=0.5, label='h_list')
    ax.set_xticks([])
    ax.set_ylabel('h')
    line3, = ax.plot([],[],lw=3)


    ax = fig.add_subplot(6,4,(13,16))
    ax.plot(t, m_list,'--',alpha=0.5, label='h_list')
    ax.set_ylabel('m')
    ax.set_xlabel('t ($ms$)')
    line4, = ax.plot([],[],lw=3)

    #fig = plt.figure()
    ax = fig.add_subplot(6,4,(17,24))
    ax.plot(n_list, v_list, '--')
    ax.set_xlabel('n')
    ax.set_ylabel('v')
    line5, = ax.plot([],[],'ro')

    Lines = [line1, line2, line3, line4, line5]
    Pathes = [[t, v_list], [t, n_list],[t,h_list],[t,m_list],[n_list,v_list]]
    init_data = [[t[0], v_list[0]],[t[0], n_list[0]],[t[0],h_list[0]],[t[0],m_list[0]],[n_list[0],v_list[0]]]
    draw_mode = ['line', 'line','line', 'line', 'dot']



    animobj = Animationcls(Lines, Pathes, init_data, fig, draw_mode)
    anim = animobj.start_animation()
    #anim.save('result{}'.format(0) + '.gif', dpi=100, writer='imagemagick', fps = 30)
