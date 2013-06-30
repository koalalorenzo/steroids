#!/usr/bin/env python
import os
from setuptools import setup

setup(name='steroids',
      version='0.11.2',
      description='Steroids: a set of tools to help python developers to build real-time ready, non-blocking, web application reducing efforts and time.',
      author='Lorenzo Setale ( http://who.is.lorenzo.setale.me/? )',
      author_email='koalalorenzo@gmail.com',
      url='https://github.com/koalalorenzo/Steroids',
      packages=['steroids', 'steroids.modules'],
      scripts=['scripts/steroids']
     )
