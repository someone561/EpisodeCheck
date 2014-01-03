"""Setup tools for EpisodeCheck,
"""

import os
import sys

# Ensure dir containing script is on PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from setuptools import setup
setup(
name = 'EpisodeCheck',
version="0.0.1",

author='someone561',
description='Checks for missing tv episodes',
url='https://github.com/someone561/EpisodeCheck',
license='unlicense',

long_description="""\
Checks if a Episodes is missing, by parsing filenames.

If you have a folder containing:
show.name.s01e01e02.avi
show.name.s01e04.avi
the script give you the information that Episode 3 is missing. This using the file parser from tvnamer
""",

packages = ['episodecheck'],

entry_points = {
    'console_scripts': [
        'episodecheck = episodecheck.episodecheck:main',
    ],
},

install_requires = ["tvnamer>=2.2.1"],

classifiers=[
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    # "License :: Unlicense",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Multimedia",
    "Topic :: Utilities",
],
)
