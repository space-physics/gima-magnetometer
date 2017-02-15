from datetime import datetime
from matplotlib.pyplot import subplots
from pytz import UTC
#
from sciencedates import tickfix

def plotmag(B):

    t = B['time'].values

    # convert xarray datetime64[ns] to Python datetime
    if isinstance(t[0],int): # datetime64[ns], seems to happen when using xarray.concat
        t = [datetime.fromtimestamp(tt/1e9,tz=UTC) for tt in t]
    elif isinstance(t[0],datetime):
        t = B['time'].values
    else:
        raise TypeError(f'unknown time class {type(B["time"][0])}')


    assert isinstance(t[0], datetime)

    fg,axs = subplots(3,1,sharex=True)

    fg.suptitle(t[0].strftime('%Y-%m-%d'))

    ax = axs[0]
    ax.plot(t,B['Bh'],label='Bh')
    ax.set_title('$B_h$')
    tickfix(B['time'],fg,ax)

    ax = axs[1]
    ax.plot(t,B['Bd'],label='Bd')
    ax.set_title('$B_d$')
    ax.set_ylabel('B [nT]')
    tickfix(t,fg,ax)

    ax = axs[2]
    ax.plot(t,B['Bz'],label='Bz')
    ax.set_title('$B_z$')
    tickfix(t,fg,ax,'%H:%M')

    ax.set_xlabel('time [UTC]')

