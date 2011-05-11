import os
import sys
if sys.version_info < (3,):
    print('Error: this is virtualenv3, whose "setup.py"'
          ' should only be run with Python 3')
    exit(1)
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    print('Note: without Setuptools installed you will have to use "python3 -m virtualenv3 ENV"')

version = '0.0'

f = open(os.path.join(os.path.dirname(__file__), 'docs', 'index.txt'))
long_description = f.read().strip()
f.close()

setup(name='virtualenv3',
      version=version,
      description='Obsolete fork of virtualenv',
      long_description=long_description,
      )
