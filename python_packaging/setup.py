import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-labeveryday", # Replace with your pypi username
    version="1.0.0",
    author="Du'An Lightfoo",
    author_email="duanl@labeveryday.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/labeveryday",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['netmiko']
)

# https://packaging.python.org/guides/distributing-packages-using-setuptools/