"""
Setup.py is a script for installing the package using setuptools.
It defines the package metadata, including name, version, author, and description.
"""

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements from a file and returns a list of package names.
    
    Args:
        file_path (str): The path to the requirements file.
        
    Returns:
        List[str]: A list of package names.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                requirement=line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")
        
    return requirement_lst

setup(
    name='MLOps-with-ETL-pipeline-Networksecurity',
    version='0.0.1',
    author='Maxie',
    author_email='hoangminh261003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)