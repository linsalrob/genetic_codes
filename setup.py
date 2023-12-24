"""
Setup.py for installing and building
"""

import os
from setuptools import setup, find_packages


def get_version():
    """
    What is the version
    :return: The version number
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION'), 'r', encoding='utf-8') as f:
        return f.readline().strip()


def get_description():
    """
    What is the description
    :return: The content of readme
    """
    with open("README.md", "r", encoding='utf-8') as fh:
        long_description = fh.read()
    return long_description

def get_requirements():
    """
    What are the requirements?
    :return: The text
    """
    reqs = []
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        for l in f:
            reqs.append(l.strip())
    return reqs

def get_data_files():
    """
    What are the datafiles
    :return:
    """
    data_files = [(".", ["README.md", "VERSION"]), ("codes", ["codes/ncbi.json", "codes/ncbi_tables.txt"])]
    return data_files


CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

def main():
    """
    The main setup code
    :return: None
    """
    setup(
        name='pygenetic_code',
        description="NCBI DNA/RNA to protein translation tabled and genetic codes",
        long_description=get_description(),
        long_description_content_type="text/markdown",
        version=get_version(),
        author="Robert Edwards",
        author_email="raedwards@gmail.com",
        platforms='any',
        keywords="DNA RNA protein bioinformatics microbiology bacteria genome genomics",
        data_files=get_data_files(),
        license='The MIT License (MIT)',
        url='https://github.com/linsalrob/genetic_codes',
        packages=find_packages(),
        entry_points={
            "console_scripts": ["pygenetic_code = pygenetic_code.cli:run"]
        },
        include_package_data=True,
        classifiers=CLASSIFIERS,
    )

if __name__ == "__main__":
    main()
