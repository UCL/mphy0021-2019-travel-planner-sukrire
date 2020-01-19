from setuptools import setup, find_packages

setup(
    name='travelplanner',
    version='0.1.0',
    author='Edward Dowling',
    author_email='edwardjdowling@gmail.com',
    packages=find_packages(exclude=['*test']),
    install_requires=['numpy', 'pandas', 'pytest', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'bussimula = travelplanner.Command:process'
            ]}
    )
