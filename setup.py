from setuptools import setup, find_packages

setup(
    name='travelplanner',
    version='1.0',
    author='Sandro Moszczynski',
    author_email='ucapsmj@ucl.ac.uk',
    packages=['travelplanner'],
    install_requires=['numpy', 'pytest', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'bussimula = travelplanner.command:process'
            ]}
    )
