#!/usr/bin/env python
req = ['nose','numpy','python-dateutil','xarray','netcdf4','sciencedates']

# %%
from setuptools import setup,find_packages

setup(name='gima_magnetometer',
      packages=find_packages(),
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
      install_requires=req,
      extras_require={'plot':['matplotlib','seaborn',]},
      python_requires='>=3.6',
	  )

