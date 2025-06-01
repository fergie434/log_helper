from setuptools import setup, find_packages

setup(
    name='log_helper',
    version='1.0.0',
    url='https://github.com/fergie434/log_helper.git',
    author='Simon Ferguson',
    author_email='author@gmail.com',
    description='Simple preconfigured wrapper for logger',
    packages=find_packages(),    
    install_requires=['logging'],
)