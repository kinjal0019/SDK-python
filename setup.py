from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name="recastai",
    version="1.1.0",
    packages=find_packages(),
    description="Recast.AI official SDK for python",
    long_description=readme,
    author="Paul Renvoise",
    author_email="paul.renvoise@recast.ai",
    url="https://github.com/RecastAI/sdk-python",
    license="MIT",
    keywords="recastai bot nlp")
