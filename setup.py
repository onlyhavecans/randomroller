#!/usr/bin/env python

from setuptools import setup
import versioneer

setup(
    name='randomroller',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    requires=['pyserial'],
    description='An extra random dice roller',
    author='David Aronsohn',
    author_email='squirrel@wearing.black',
    url='https://github.com/onlyhavecans/randomroller',
    packages=['randomroller'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    entry_points={
        'console_scripts': ['rr = randomroller.cli:main'],
    },
)
