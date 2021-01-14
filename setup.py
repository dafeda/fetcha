import re

from setuptools import setup, find_packages

with open("fetcha/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="fetcha",
    version=version,
    description="Talk to SSB using Python.",
    url="https://github.com/dafeda/fetcha",
    author="Feda Curic",
    author_email="feda.curic@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pyjstat"],
)
