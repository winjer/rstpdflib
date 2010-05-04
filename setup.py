#! /usr/bin/env python

from distutils.core import setup

setup(name="rst2pdf",
    version="1.0",
    description="Convert restructured text to PDF, with styles",
    author="Doug Winter",
    author_email="doug@isotoma.com",
    packages=['rstpdflib', 'rstpdflib.scripts', 'rstpdflib.plugins'],
    scripts=['bin/rst2pdf'],
    package_data={'rstpdflib': ['templates/*.ini', 'templates/*.png', 'templates/*.pdf']},
)


