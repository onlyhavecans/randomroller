#!/usr/bin/env python

import os
from setuptools import setup
import versioneer

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='randomroller',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    requires=['pyserial'],
    description='An extra random dice roller',
    long_description=readme,
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
    install_requires=['pyserial']
)
