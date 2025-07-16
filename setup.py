from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

import os 

setup(
    name='universalpython',
    version='1.1',
    packages=['urdu_python',],
    description='UniversalPython kernel for Jupyter',
    long_description=readme,
    author='Saad Bazaz',
    author_email='saadbazaz@hotmail.com',
    url='https://github.com/UniversalPython/UniversalPython',
    install_requires=[
        'jupyter_client', 
        'IPython', 
        'ipykernel',
        'urdupython'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
