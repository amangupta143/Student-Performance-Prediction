from setuptools import setup, find_packages
from typing import List

# Get requirements from requirements.txt
HYPHEN_E_DOT = '-e .'
def get_requirements(path:str) -> List[str]:
    with open(path, 'r') as f:
        requirements = [line.strip() for line in f.readlines()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements
    
# Setup package
setup(
    name='student-performance-prediction',
    version='0.1.0',
    description='Student Performance Prediction',
    author='Aman Gupta',
    author_email='amangupta.main@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)