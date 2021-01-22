#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from pyhinavrophonetic import __version__


    setup(name='pyhinavrophonetic',
          version='2.0.0',
          description='Python implementation to convert phonetic to hindi',
          long_description=open('README.rst', 'rt').read(),
          author='Subrata Sarkar',
          author_email='subrotosarkar32@gmail.com',
          url='https://bitbucket.org/SubrataSarkar32/pyhinavrophonetic/',
          packages=find_packages(),
          package_data = {'pyhinavrophonetic': ['*.rst', 'resources/*.json']},
          include_package_data = True,
          license='GNU GPL v3 or later',
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6.5',
            ]
          )

except ImportError:
    print('Install setuptools')
