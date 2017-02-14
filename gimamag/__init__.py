from pathlib import Path
import netCDF4 as nc
#from xarray import DataArray
from numpy import array
from datetime import datetime,timedelta
from dateutil.parser import parse
import xarray as xr
#
from sciencedates import forceutc

def readgima(flist,tlim):
    """
    Helper function to concatenate hourly file data
    """
    if isinstance(flist,(str,Path)):
        flist = [flist]

    flist = [Path(f).expanduser() for f in flist]

    for fn in flist:
        B = readgimafile(fn,tlim)

        if fn.samefile(flist[0]):
            Bs = B
        else:
            Bs = xr.concat([Bs,B],dim='time')

    return Bs

def readgimafile(fn, tlim):
    """
    main file reading function
    """
    fn = Path(fn).expanduser()
    if not fn.is_file():
        raise FileNotFoundError(f'{fn} does not exist')
#%% date from filename -- only way
    d0 = forceutc(datetime.strptime(fn.stem[-13:-3],'%Y_%m_%d'))

    with nc.Dataset(str(fn),'r') as f:
#%% load by time
        th = f['time'][:]
        t=[]
        for h in th:
            hour = int(h)
            second = (h-hour)*3600
            t.append(d0 + timedelta(hours=hour,
                                    seconds=second))

        t=array(t)
        if tlim is not None and len(tlim)==2:
            if isinstance(tlim[0], str):
                tlim = [forceutc(parse(t)) for t in tlim]
            tind = (tlim[0] <= t) & (t <= tlim[1])
        else:
            tind = slice(None)
#%% load data
        B = xr.Dataset({'Bh':(['time'], f['hcomp'][tind]),
                        'Bd':(['time'], f['dcomp'][tind]),
                        'Bz':(['time'], f['zcomp'][tind])},
                        coords={'time':t[tind]})

    return B
