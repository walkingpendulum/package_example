from setuptools import setup, find_packages

from palindrome_checker import __version__


setup(
    name='palindrome_checker',
    version=__version__,
    python_requires='>=2.7',     # here you can place python version restrictions
    url='https://github.com/walkingpendulum/package_example',
    packages=find_packages(exclude=('tests',)),
    install_requires=open('requirements.txt').read().split(),
    entry_points={
        'console_scripts': [
            'check_palindrome = palindrome_checker.entrypoints:checker',
        ],
    },
)
