import itertools

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os.path as op
import scipy.io.wavfile as scwav


def data_gen(time, beread):
    for x, y in zip(time, beread):
        yield x, y

def init():
    ax.set_ylim(-42000, -12000)
    ax.set_xlim(0, 100)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,



def init_2_col(filename):
#    folder = '/mnt/d/images/tmpdata/data_matplotlib'
#    folderwin = 'D:/images/tmpdata/data_matplotlib'
    #L1 = folder + '/L1_Strain.wav'
    L = op.abspath(filename)
    Lread = np.array(scwav.read(L)[1], dtype=object)
    print(Lread)

    time = np.arange(0, len(Lread))

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.grid(which='major')
    xdata, ydata = [], []
    return fig, ax, xdata, ydata, line,

def run(data, xdata, ydata, line, ax):
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)#倍增扩容……
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,




if __name__ == '__main__':

    fig, ax, xdata, ydata, line, = init_2_col(filename='/mnt/d/images/tmpdata/data_matplotlib')
    ani = animation.FuncAnimation(fig, run, data_gen, interval=1, init_func=init)
    ax.set_title('Wave Shape', fontsize=12)
    ax.set_alpha(0.5)
    ani.save('waver.gif', writer='pillow')
    plt.show()
#Animation: