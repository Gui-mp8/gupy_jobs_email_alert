#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="gupy-jobs-alert",
    version="1.0.0",
    description="Application that sends jobs alerts to the email",
    author="Guilherme Machado Pires",
    url="https://github.com/Gui-mp8",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.12.2",
        "bs4==0.0.1",
        "certifi==2023.5.7",
        "charset-normalizer==3.2.0",
        "idna==3.4",
        "requests==2.31.0",
        "soupsieve==2.4.1",
        "urllib3==2.0.4",
    ],
)
