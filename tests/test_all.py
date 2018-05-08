#!/usr/bin/env python
from pathlib import Path
from datetime import datetime
import numpy as np
import numpy.testing as npt
from gimamag import readgima

fn = Path(__file__).parent / 'poker_2017_11_16_10.nc'
t=np.datetime64(datetime(2017, 11, 16, 10, 0, 2, 1600))

def test_readmag():
    B = readgima(fn)
    Bh2 = B.sel(dir='Bh')[2]
    npt.assert_allclose(Bh2, 12119.9)
# %%
    B2 = readgima(fn,('2017-11-16T10:00:02','2017-11-16T10:00:02.5'))

    assert B2.sel(dir='Bh')==Bh2


if __name__ == '__main__':
    npt.run_module_suite()
