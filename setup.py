import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # the distribution name of your package
    name="packaging-example",
    # the package version"
    version="0.0.1",
    # author name
    author="Author Name",
    author_email="author@example.com",
    # one-sentence summary of the package
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)