from setuptools import find_packages,setup
from typing import List
def get_requirements(filepath:str)->List[str]:
    requirement=[]
    with open(filepath) as fp:
        requirement=fp.readlines()
        requirement=[ele.replace('/n','') for ele in requirement]

        if '-e .' in requirement:
            requirement.remove('-e .')
        return requirement

setup(
    name='diamondpriceprediction',
    version='0.0.1',
    author='saisachin',
    author_email='doddasaisachin@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)