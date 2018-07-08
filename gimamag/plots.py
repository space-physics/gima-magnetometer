import xarray as xr
from matplotlib.pyplot import subplots


def plotmag(B: xr.DataArray):

    fg, axs = subplots(3, 1, sharex=True)

    for d, a in zip(B.dir, axs):
        B.sel(dir=d).plot(ax=a)
        a.set_title('')
        a.set_xlabel('')
        a.set_ylabel(f'{d.item()} [nT]')

    axs[-1].set_xlabel('time [UTC]')
