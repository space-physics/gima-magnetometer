from pathlib import Path
import netCDF4 as nc
import numpy as np
from datetime import datetime, timedelta
from dateutil.parser import parse
import xarray as xr
from typing import List, Union


def readgima(flist: List[Path], tlim: List[Union[str, datetime]] = None):
    """
    Helper function to concatenate hourly file data

    NOTE: could just use tarfile to avoid extracting files
    """
    if isinstance(flist, (str, Path)):
        flist = [flist]

    flist = [Path(f).expanduser() for f in flist]

    for fn in flist:
        B = readgimafile(fn, tlim)

        if fn.samefile(flist[0]):
            Bs = B
        else:
            Bs = xr.concat([Bs, B], dim='time')

    return Bs


def readgimafile(fn: Path,
                 tlim: List[Union[str, datetime]] = None) -> xr.DataArray:
    """
    main file reading function
    """
    fn = Path(fn).expanduser()
    if not fn.is_file():
        raise FileNotFoundError(f'{fn} does not exist')
# %% date from filename -- only way
    d0 = datetime.strptime(fn.stem[-13:-3], '%Y_%m_%d')

    with nc.Dataset(fn, 'r') as f:
        # %% load by time
        th = f['time'][:]
        t = []
        for h in th:
            hour = int(h)
            second = (h-hour)*3600
            t.append(d0 + timedelta(hours=hour,
                                    seconds=second))

        tind: Union[bool, slice]
        t = np.asarray(t)
        if tlim is not None and len(tlim) == 2:
            if isinstance(tlim[0], str):
                tlim = [parse(t) for t in tlim]  # type: ignore
            tind = (tlim[0] <= t) & (t <= tlim[1])  # type: ignore
        else:
            tind = slice(None)
# %% load data
        B = xr.DataArray(np.column_stack((f['hcomp'][tind],
                                          f['dcomp'][tind],
                                          f['zcomp'][tind])),
                         coords={'dir': ['Bh', 'Bd', 'Bz'],
                                 'time': t[tind]},
                         dims=['time', 'dir'])

    return B
