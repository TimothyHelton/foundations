#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from codecs import open
import os.path as osp
from setuptools import setup, find_packages
import foundations


here = osp.abspath(osp.dirname(__file__))
with open(osp.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='foundations',
        version='1.0.0',
        description='K2 Data Science Bootcamp Foundations Coursework',
        author='Timothy Helton',
        author_email='timothy.j.helton@gmail.com',
        license='BSD',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Build Tools',
            ],
        keywords='data science education',
        packages=find_packages(exclude=['docs', 'tests*']),
        install_requires=[
            'strumenti',
            ],
        package_dir={'foundations': 'foundations'},
        include_package_data=True,
    )


if __name__ == '__main__':
    pass
