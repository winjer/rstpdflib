#! /usr/bin/env python

from setuptools import setup, find_packages

version = "1.0"

setup(name="rstpdflib",
    version = version,
    description="Convert restructured text to PDF, with styles",
    long_description = open("README.rst").read(),
    author="Doug Winter",
    author_email="doug@isotoma.com",
    packages = find_packages(exclude=['ez_setup']),
    package_data = {
        '': ['README.rst'],
        'rstpdflib': ['templates/example.ini'],
    },
    include_package_data = False,
    zip_safe = False,
    scripts=['bin/rst2pdf'],
)


