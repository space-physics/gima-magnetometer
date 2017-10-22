#!/usr/bin/env python
req = ['nose','numpy','python-dateutil','xarray','matplotlib','seaborn','netcdf4']
pipreq= ['sciencedates']

import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)
# %%
from setuptools import setup

setup(name='gima_magnetometer',
      packages=['gimamag'],
      version = '0.6',
      description='Plotting and analysis of UAF GIMA Magnetometer data',
      author = 'Michael Hirsch, Ph.D.',
      url = 'https://github.com/scivision/gima-magnetometer',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3.6',
      ],
      install_requires=req+pipreq,
	  )

