import numpy as np
import matplotlib.pyplot as plt
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.functions import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.plotutils import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.variables import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.animutils import Animationcls

#I_list = [0,0.3,0.4,0.8,1.5]
I_list = [0.55629606846978]
ind = 0
for I in I_list:

    fig = plt.figure()
    ax = fig.add_subplot(3,3,(1,8))
    v_list, w_list, v_dot_list, w_dot_list = run_experiment(v,w,I,t_total, dt)
    ax.plot(w_list,v_list, lw=3)
    ax.set_xlabel('w')
    ax.set_ylabel('v')
    arrow_plotter(v_range, w_range,I,ax,n=50)



    phase_line, = ax.plot([],[],'ro')

    ax = fig.add_subplot(3,3,3, title = 'v_plot')
    ax.set_xlim([0,t_total])
    ax.set_ylim([-2,2])
    ax.set_ylabel('v')
    ax.set_xlabel('t')
    v_track, = ax.plot([],[])


    ax = fig.add_subplot(3,3,9, title = 'w_plot')
    ax.set_xlim([0,t_total])
    ax.set_ylim([-2,2])
    ax.set_ylabel('w')
    ax.set_xlabel('t')
    #ax.autoscale_view(scaley=True)
    ax.autoscale(axis='y')
    w_track, = ax.plot([],[])


    ax = fig.add_subplot(3,3,6)
    ax.text(0,0,'I = {}'.format(I), fontsize=12, horizontalalignment='center', verticalalignment = 'center')
    ax.set_xlim([-0.5,0.5])
    ax.set_ylim([-0.5,0.5])
    ax.set_axis_off()

    Lines = [phase_line, v_track, w_track]
    Pathes = [[w_list, v_list],[t, v_list], [t,w_list]]
    initial = [[w_list[0], v_list[0]],[t[0],v_list[0]],[t[0],w_list[0]]]
    draw_mode = ['dot', 'line', 'line']


    animobj = Animationcls(Lines,Pathes, initial, fig, draw_mode)
    anim = animobj.start_animation()
    #anim.save('result{}'.format(ind) + '.gif', dpi=100, writer='imagemagick', fps = 30)

    #ax = fig.add_subplot(3,3,3)
    #v_track = ax.plot()



    #plt.xlim(w_range[0], w_range[1])
    #plt.ylim(v_range[0], v_range[1])
    #plt.savefig('I_{}.png'.format(ind))
    #plt.show()

    ind +=1
