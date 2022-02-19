from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='scorewithimage',
    version='0.1.3',
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    include_package_data=True
)