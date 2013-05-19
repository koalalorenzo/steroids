#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(name='steroids',
      version='0.3',
      description='',
      author='Lorenzo Setale ( http://who.is.lorenzo.setale.me/? )',
      author_email='koalalorenzo@gmail.com',
      url='https://github.com/koalalorenzo/Steroids',
      packages=['steroids'],
      scripts=['scripts/steroids']
     )
