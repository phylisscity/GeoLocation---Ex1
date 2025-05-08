from setuptools import setup, find_packages

setup(
    name='geomodule',
    version='1.0.0',
    description='A GPS matching module that finds the closest point using the Haversine formula.',
    author='Phyliss',
    packages=find_packages(),  # Automatically includes geomodule/
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
