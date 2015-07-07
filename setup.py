
from setuptools import setup, find_packages

setup(
    name='smis',
    version='0.0.4',
    description='Simple MIS Library',
    long_description='A simple library to access Autodesk InfraWorks 360 Model Information Service.',
    author='Isaac Rodriguez',
    author_email=isaac.rodriguez@autodesk.com
    classifiers = ['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 2.7'],
    url='https://github.com/CurroRodriguez/smis-python',
    packages=find_packages('source/smis'),
    install_requires=['requests>=2.7', 'requests-oauthlib>=0.5']
)
