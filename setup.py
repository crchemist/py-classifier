import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'py-classifier',
   version = '0.0.1',
   author = 'Antip Team',
   author_email = 'didipk@gmail.com',
   description = ('py-classifier library provides bayesian classification on a given text similar to many SPAM/HAM filtering technique.'),
   license = 'BSD',
   keywords = 'bayesian filter api',
   url = 'https://github.com/crchemist/py-classifier',
   packages=['py_classifier_api',],
   long_description=read('README'),
   classifiers=['Programming Language :: Python :: 3',]
)
