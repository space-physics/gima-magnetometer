#!/usr/bin/env python
from matplotlib.pyplot import show
#
from gimamag import readgima
from gimamag.plots import plotmag
import seaborn as sns
sns.set_context('talk',font_scale=1.5)
sns.set_style('whitegrid')

"""
./LoadGIMA.py ~/data/2007-03-23/mag/poker_2007_03_23_11.nc -t 2007-03-23T11:17 2007-03-23T11:28
"""

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='reading UAF Geophysical Institute GIMA magnetometer data')
    p.add_argument('ncfn',help='netCDF data file name to read')
    p.add_argument('-t','--tlim',help='time window to zoom plot in on',nargs=2)
    p.add_argument('-v','--verbose',action='store_true')
    p = p.parse_args()

    t,Bh,Bd,Bz = readgima(p.ncfn, p.tlim)
    plotmag(t,Bh,Bd,Bz)
#%%

    show()
