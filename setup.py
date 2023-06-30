from setuptools import find_packages, setup

with open('requirements.txt', 'r') as f:
    req = [p for p in f.readlines()]

setup(
    name='mcsim',
    version='1.1.0',
    install_requires=req,
    packages=find_packages(exclude='data')
)