"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

import opencmiss.zinc.context

APP = ['opencmiss/neon/neon.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
#    'frameworks': ['/Users/hsor001/work/opencmiss-software/zinc-software/zinc/library-build-make/core/libzinc.r11285M.3.0.1.dylib']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
