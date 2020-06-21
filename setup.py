from setuptools import setup,find_packages

setup(
    name='my-package',
    version='2.0',
    description='VLutsenko packege for DPP lab 10',
    author='Vladyslav Lutsenko',
    author_email='245817@student.pwr.edu.pl',
    packages=find_packages(),
    install_requires=['requests']

)