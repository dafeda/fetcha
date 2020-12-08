import re

from setuptools import setup, find_packages

with open("fetcha/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="fetcha", version=version, packages=find_packages(), include_package_data=True
)
