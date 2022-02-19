from setuptools import setup, find_packages

setup(
    name='scorewithimage',
    version='0.1.5',
    packages=find_packages(),
    install_requires=["IPython", "pandas"],
    include_package_data=True
)