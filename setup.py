from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='pratac',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pratac = pratac.__main__:main'
        ]
    },
    long_description=description,
    long_description_content_type='text/markdown',
)
