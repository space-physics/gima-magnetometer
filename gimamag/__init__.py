from pathlib import Path
from netCDF4 import Dataset
#from xarray import DataArray
from numpy import array
from datetime import datetime,timedelta
from dateutil.parser import parse
#
from sciencedates import forceutc

def readgima(fn, tlim):
    """
    """
    fn = Path(fn).expanduser()
    if not fn.is_file():
        raise FileNotFoundError(f'{fn} does not exist')
#%% date from filename -- only way
    d0 = forceutc(datetime.strptime(fn.stem[-13:-3],'%Y_%m_%d'))

    with Dataset(str(fn),'r') as f:
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
        t = t[tind]
        Bh = f['hcomp'][tind]
        Bd = f['dcomp'][tind]
        Bz = f['zcomp'][tind]


    return t,Bh,Bd,Bz
