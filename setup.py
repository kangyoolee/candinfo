from setuptools import setup, find_packages

setup(name='candinfo',
    version='1.0.0a',
    url='https://github.com/kangyoolee/candinfo.py',
    author='kangyoolee',
    author_email='me@kangyoo.kr',
    description='Korea Candidate Unofficial API Wrapper ', 
    packages=find_packages(exclude=['']), 
    long_description=open('README.md').read(), 
    install_requires=['requests','xmltodict'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)