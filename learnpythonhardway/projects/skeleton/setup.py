#!/usr/bin/env python3
# --coding:utf-8 --

try:
    from setuptools import setup
except ImportError:
    form distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Fan Shuhan',
        'url': 'URL to get it at.',
        'download_url': 'where to download it.',
        'email': 'fanshuhanohno@gmail.com',
        'version': '0.1',
        'install_required': ['nose'],
        'package':['name'],
        'scripts': [],
        'name': 'project name'
        }

setup(**config)
