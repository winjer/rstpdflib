#! /usr/bin/env python

from setuptools import setup, find_packages

version = "1.0"

setup(name="rstpdflib.plugins.isotoma",
    version=version,
    description="Isotoma document templates for rstpdflib",
    url="http://github.com/winjer/rstpdflib",
    long_description=open("README.rst").read(),
    author="Doug Winter",
    author_email="doug@isotoma.com",
    packages = find_packages(exclude=['ez_setup']),
    package_data = {
        '': ['README.rst'],
        'rstpdflib.plugins.isotoma': ['templates/*.ini', 'templates/*.png'],
    },
    namespace_packages = ['rstpdflib', 'rstpdflib.plugins'],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'rstpdflib',
        'ConfigObj',
    ],
)

