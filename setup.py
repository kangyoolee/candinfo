import setuptools

setuptools.setup(
    name="candinfo",
    version="1.0.0a",
    license='MIT',
    author="kangyoolee",
    author_email="me@kangyoo.kr",
    description="Korea Candidate Unofficial API Wrapper",
    long_description=open('README.md').read(),
    url="https://github.com/kangyoolee/candinfo",
    packages=['requests','xmltodict'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)