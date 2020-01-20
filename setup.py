from setuptools import setup, find_packages

setup(
    name='travelplanner',
    version='0.0.0',
    author='Sandro Moszczynski',
    author_email='ucapsmj@ucl.ac.uk',
    packages=find_packages(exclude=['*test']),
    install_requires=['numpy', 'pytest', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'bussimula = travelplanner.command:process'
            ]}
    )