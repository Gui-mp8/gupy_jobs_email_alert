#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="gupy-jobs-alert",
    version="1.2.0",
    description="Application that sends jobs alerts to the email",
    author="Guilherme Machado Pires",
    url="https://github.com/Gui-mp8",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.12.2",
        "lxml==4.9.3",
        "requests==2.31.0",
        "pytest==7.4.2",
        "pydantic==2.3.0"
    ],
)
