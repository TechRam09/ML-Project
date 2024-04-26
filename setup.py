from setuptools import find_packages,setup
from typing import List

E_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of reqirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if E_dot in requirements:
            requirements.remove(E_dot)     
    
    return requirements       
       
setup(
    
    name='MLproject',
    version='0.0.1',
    author='Shreeram',
    author_email='nsshreeram@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirement.txt')
)