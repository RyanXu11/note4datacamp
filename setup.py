#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Ryan Xu",
    author_email='ryan.y.xu@hotmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Python package to help with note-taking in DATACAMP courses.",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='note4datacamp',
    name='note4datacamp',
    packages=find_packages(include=['note4datacamp', 'note4datacamp.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/RyanXu11/note4datacamp',
    version='1.0.0',
    zip_safe=False,
)
