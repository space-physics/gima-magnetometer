#!/usr/bin/env python
install_requires = ['numpy','python-dateutil','xarray','netcdf4',
          'sciencedates']
tests_require=['pytest','nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='gima_magnetometer',
      packages=find_packages(),
      version = '0.6.1',
      description='Plotting and analysis of UAF GIMA Magnetometer data',
      author = 'Michael Hirsch, Ph.D.',
      url = 'https://github.com/scivision/gima-magnetometer',
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Topic :: Scientific/Engineering :: GIS',
      ],
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'plot':['matplotlib','seaborn',],
                      'tests':tests_require},
      python_requires='>=3.6',
      scripts=['LoadGIMA.py'],
	  )

