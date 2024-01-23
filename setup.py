from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace('\n',"")for r in requirements]
        
    return requirements



setup(
name='Machine learning project',
version='0.0',
author='Zeeshan Firdousi',
author_email='zeeshanfirdousi7086@gmail.com',
packages=find_packages(),
install_requires=get_requirements('Requirements.txt')
)