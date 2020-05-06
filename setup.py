import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gluemotion",
    version="0.0.1-alpha",
    author="Lukas Schmid",
    author_email="lukas.m.schmid@gmail.com",
    description="Glue Emotion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Luke31/gluemotion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
