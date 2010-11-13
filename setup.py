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

version = '1.3.4.2'

f = open(os.path.join(os.path.dirname(__file__), 'docs', 'index.txt'))
long_description = f.read().strip()
f.close()

setup(name='virtualenv3',
      version=version,
      description="Virtual Python 3 Environment builder",
      long_description=long_description,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
      ],
      keywords='setuptools deployment installation distutils',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='http://bitbucket.org/brandon/virtualenv3/',
      license='MIT',
      py_modules=['virtualenv3'],
      ## Hacks to get the package data installed:
      packages=[''],
      package_dir={'': '.'},
      package_data={'': ['support-files/*-py%s.egg' % sys.version[:3]]},
      zip_safe=False,
      entry_points="""
      [console_scripts]
      virtualenv3 = virtualenv3:main
      """,
      )
