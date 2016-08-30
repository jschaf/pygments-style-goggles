# -*- coding: utf-8 -*-
from distutils.core import setup
import setuptools
import sys


_version = '0.1'
_packages = ['style']

_short_description = "pygments-style-goggles is a colorful style for pygments."


_classifiers = (
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Text Processing :: Filters'
)


_install_requires = [
    'pygments>=2'
]

setup(
    name='pygments-style-goggles',
    url='https://github.com/jschaf/pygments-style-goggles',
    author='Joe Schafer',
    author_email='joe@jschaf.com',
    description=_short_description,
    version=_version,
    packages=_packages,
    install_requires=_install_requires,
    license='GPLv2',
    download_url=("https://github.com/jschaf/pygments-style-goggles/tarball/v" +
                  str(_version)),
    classifiers=_classifiers,
    keywords='pygments syntax highlighting',
    entry_points={
        'pygments.styles': [
            'goggles = style:GogglesStyle',
        ]
    }
)
