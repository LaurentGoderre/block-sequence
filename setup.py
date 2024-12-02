from distutils.core import setup

setup(name='blocksequence',
  version='0.1',
  description='Sequence a collection of blocks in a parent geography',
  maintainer='Reginald Maltais',
  maintainer_email='reginald.maltais2@canada.ca',
  url='https://github.com/statcan/block-sequence',
  packages=['blocksequence',],
  license='MIT',
  long_description=open('README.md').read(),
  install_requires=[
    "click == 6.7",
    "click-log == 0.3.2",
    "click-plugins == 1.0.3",
    "Fiona == 1.7.13",
    "geopandas == 0.4.0",
    "matplotlib == 2.2.3",
    "networkx == 2.2",
    "numpy == 1.22.0",
    "pandas == 0.23.4",
    "pyproj == 1.9.6",
    "pytest == 4.0.1",
    "Shapely == 1.6.4.post2",
  ],
  entry_points={
    'console_scripts': [
      'blocksequence=blocksequence.cli:start'
    ]
  }
)
