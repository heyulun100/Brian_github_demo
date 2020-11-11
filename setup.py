__author__ = 'Brian M Anderson'
# Created on 9/15/2020


from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ProjectName',
    author='Brian Mark Anderson',
    author_email='bmanderson@mdanderson.org',
    version='0.0.1',
    description='A brief description of the project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'RandomPackage': 'src/RandomPackage'},
    packages=['RandomPackage'],
    include_package_data=True,
    url='https://github.com/brianmanderson/Project_Template',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    install_requires=required,
)
