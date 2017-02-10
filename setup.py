#!/usr/bin/env python
from setuptools import setup

req = ['msp_aurora','sciencedates',
        'nose','numpy','python-dateutil','xarray','matplotlib','seaborn','netcdf4']

setup(name='gima_magnetometer',
      packages=['gimamag'],
      version = '0.5',
      description='Plotting and analysis of UAF GIMA Magnetometer data',
      author = 'Michael Hirsch, Ph.D.',
      url = 'https://github.com/scienceopen/gima-magnetometer',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3.6',
      ],
      install_requires=req,
      dependency_links=[
      'https://github.com/scienceopen/meridian-spectrometer-reader/tarball/master#egg=msp_aurora'
      ],
	  )

