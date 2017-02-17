#!/usr/bin/env python
from matplotlib.pyplot import show
#
from gimamag import readgima
from gimamag.plots import plotmag
import seaborn as sns
sns.set_context('talk',font_scale=1.5)
sns.set_style('whitegrid')
"""
GIMA data download:
https://www.asf.alaska.edu/magnetometer/download/

./LoadGIMA.py ~/data/2013-04-14/mag/poker_2013_04_14_08.nc  ~/data/2013-04-14/mag/poker_2013_04_14_09.nc -t 2013-04-14T08:35 2013-04-14T09:25:00.1

./LoadGIMA.py ~/data/2013-04-14/mag/poker_2013_04_14_08.nc -t 2013-04-14T08:20 2013-04-14T08:35:00.1

./LoadGIMA.py ~/data/2011-03-01/mag/poker_2011_03_01_09.nc ~/data/2011-03-01/mag/poker_2011_03_01_10.nc -t 2011-03-01T09:45 2011-03-1T10:30:00.1

./LoadGIMA.py ~/data/2007-03-23/mag/poker_2007_03_23_11.nc -t 2007-03-23T11 2007-03-23T12
"""

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='reading UAF Geophysical Institute GIMA magnetometer data')
    p.add_argument('ncfn',help='netCDF data file name to read',nargs='+')
    p.add_argument('-t','--tlim',help='time window to zoom plot in on',nargs=2)
    p.add_argument('-v','--verbose',action='store_true')
    p = p.parse_args()

    B = readgima(p.ncfn, p.tlim)
    plotmag(B)
#%%

    show()
