from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name = "structures",
    version = "0.0.1",
    author = "Pedro Sousa",
    author_email = "pedroteosousa@gmail.com",
    description = "Implementation of various data structures",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/pedroteosousa/python-structures",
    packages = find_packages(where = "src", exclude = ["tests"]),
    package_dir = {"" : "src"},
    classifiers = [
        "Programming Language :: Python :: 3",
    ],
)
