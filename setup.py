from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="geometry",
    version="0.1.0",
    install_requires=read_requirements(),
    packages=find_packages(),
    include_package_data=True
)
