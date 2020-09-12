import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lsystem",  # Replace with your own username
    version="0.0.1",
    author="Andrew Truong",
    description="A package to help render and manage L-Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adhtruong/l-system",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
