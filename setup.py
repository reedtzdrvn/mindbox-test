from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="geometry_calculator",
    version="0.1.0",
    install_requires=requirements,
    packages=find_packages()
)
