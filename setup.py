# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='ocrd_anybaseocr',
    version='0.0.1',
    description='Tweaked ocropus scripts',
    author='Saqib Bukhari',
    author_email='saqib.bukhari@dfki.de',
    url='https://github.com/kba/ocrd_dfkitools',
    license='Apache License 2.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=open('requirements.txt').read().split('\n'),
    packages=['ocrd_anybaseocr'],
    package_data={
        '': ['*.json']
    },
    entry_points={
        'console_scripts': [
            'ocrd-anybaseocr-binarize = ocrd_anybaseocr.cli.binarize:main',
            'ocrd-anybaseocr-crop     = ocrd_anybaseocr.cli.cropping:main',
            'ocrd-anybaseocr-deskew   = ocrd_anybaseocr.cli.deskew:main',
        ]
    },
)
