from msp_aurora.plots import tickfix
from matplotlib.pyplot import subplots

def plotmag(t,Bh,Bd,Bz):
    if len(t)==0:
        return

    fg,axs = subplots(3,1,sharex=True)

    ax = axs[0]
    ax.plot(t,Bh,label='Bh')
    ax.set_title('$B_h$')

    ax = axs[1]
    ax.plot(t,Bd,label='Bd')
    ax.set_title('$B_d$')
    ax.set_ylabel('B [nT]')


    ax = axs[2]
    ax.plot(t,Bz,label='Bz')
    ax.set_title('$B_z$')

    ax.set_xlabel('time [UTC]')
    tickfix(t,fg,ax)
