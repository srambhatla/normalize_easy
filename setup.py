import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "normalize_easy",
    version = "0.0.1",
    author = "Sirisha Rambhatla",
    author_email = "rambh002@umn.edu",
    description = ("This package implements normc() and normr() functions to \
    easily normalize columns and rows respectively."),
    license = "BSD",
    keywords = "normr normc normalize rows columns math matrix linear algebra \
    MATLAB",
    url = "https://github.com/srambhatla/normalize_easy",
    packages = ['normalize_easy'],
    long_description = read('README.md'),
    install_requires = ['sklearn', 'numpy'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)