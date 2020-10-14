# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="strandet",
    version="0.1.0",
    description="Ascii text adventure game by dynnamighties (Jr and Sr)",
    license="MIT",
    author="Kjetil Flovild-Midtlie",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
