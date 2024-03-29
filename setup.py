"""Packaging information."""


from os.path import abspath, dirname, join, normpath
from subprocess import call
from sys import exit

from setuptools import Command, setup


class TestCommand(Command):

    description = 'run all tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run the test suite."""
        exit(call(['py.test', '--cov', 'brute']))


setup(

    # Basic package information:
    name = 'brute',
    version = '1.0.0',
    py_modules = ['brute'],

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [],

    # Test harness:
    cmdclass = {
        'test': TestCommand,
    },

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/brute',
    keywords = 'python security bruteforce hash hack',
    description = 'Simple brute forcing in Python.',
    long_description=open(normpath(join(dirname(abspath(__file__)), 'README.md'))).read(),
    long_description_content_type='text/markdown',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)
