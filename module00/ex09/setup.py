from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A python library for counting values in iterables",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="bjacobs",
    author_email="bjacobs@student.codam.nl",
    url="https://github.com/bjacobs/ft_package",
    packages=find_packages(),
    python_requires=">=3.10",
    license="MIT",
    classifies=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approbed :: MIT Lincense",
    ]
)
