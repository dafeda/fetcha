import re

from setuptools import setup, find_packages

with open("fetcha/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="fetcha",
    version=version,
    description="Talk to SSB using Python.",
    long_description=long_description,
    long_description_content_type='text/markdown',    
    url="https://github.com/dafeda/fetcha",
    author="Feda Curic",
    author_email="feda.curic@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pyjstat"],
)
