from setuptools import setup, find_packages

setup(
    name="nyc-parser",
    version="0.1.0",
    packages=find_packages(),
    description="A parser for New York City addresses and BBL values",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ian Shiland",
    author_email="ishiland@gmail.com",
    url="https://github.com/ishiland/nyc-parser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
