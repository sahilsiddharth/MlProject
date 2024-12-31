from setuptools import find_packages,setup
from typing import List
HYPEN_DOT_E='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirement.
    '''
    requirement=[]
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()  # Remove any extra whitespace or newline characters
            if line != HYPEN_DOT_E:
                requirement.append(line)
    
    return requirement

setup(
    author="Siddharth",
    version="0.0.1",
    name="mlproject",
    author_email="sahilsiddharth@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)