#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mosmetro',
      version='1.0',

      author='Dmitry Karikh',
      author_email='the.dr.hax@gmail.com',
      license='GNU GPLv3',
      url='https://github.com/mosmetro-android/mosmetro-python',

      install_requires=['requests', 'pyquery', 'fake_useragent==0.1.7', 'urllib3', 'bs4'],

      packages=find_packages(),
      package_data={'mosmetro': ['res/*']},
      include_package_data=True,

      entry_points='''
        [console_scripts]
        mosmetro=mosmetro.__main__:main
      ''',
     )
