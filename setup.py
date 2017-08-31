#!/usr/bin/env python

from setuptools import setup

setup(
    name='randomroller',
    version='1.0',
    requires=['pyserial'],
    description='An extra random dice roller',
    author='David Aronsohn',
    author_email='WagThatTail@Me.com',
    url='https://github.com/onlyhavecans/randomroller',
    packages=['randomroller'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    entry_points={
        'console_scripts': ['rr = randomroller.cli:main'],
    },
)
