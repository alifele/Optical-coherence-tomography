

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc


class Animationcls():

    def __init__(self,Lines,Pathes,init_data, fig, draw_mode):

        # Lines  --> [phase_line, v_line, w_line]
        # Pathes contian the tuples that the first element is the t_list and second element is x_list
        self.L = len(Lines)
        self.LP = len(Pathes)
        self.Lines = [1] * self.L
        self.Pathes = [1] * self.LP
        self.init_data = [1] * self.L
        self.draw_mode = draw_mode

        for i in range(self.L):
            self.Lines[i] = Lines[i]

        for i in range(self.LP):
            self.Pathes[i] = Pathes[i]

        for i in range(self.L):
            self.init_data[i] = init_data[i]

        self.fig = fig



    def init(self):

        for i in range(self.L):
            self.Lines[i].set_data(self.init_data[i])

        #self.Lines_list[0].set_data([0],[0])
        #self.Lines_list[1].set_data(t[-50], x[-50])
        #self.Lines_list[2].set_data([0],[0])
        return self.Lines


    def animate(self, i):
        speed = 50
        for ii in range(self.L):
            if self.draw_mode[ii] == 'line':
                self.Lines[ii].set_data(self.Pathes[ii][0][:speed * i],self.Pathes[ii][1][:speed * i])
            else:
                self.Lines[ii].set_data(self.Pathes[ii][0][speed * i],self.Pathes[ii][1][speed * i])

        #self.Lines_list[1].set_data(t[i],x[i])
        #self.Lines_list[1].set_data(t[-i],x[-i])
        #self.Lines_list[2].set_data([0], x[i])
        return self.Lines

    def start_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func = self.init,frames=200, interval=45, blit=True, repeat= True)
        #Writer = animation.writers['ffmpeg']
        #writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1500)
        #anim.save('lines.mp4', writer=writer)
        plt.show()
        return anim
