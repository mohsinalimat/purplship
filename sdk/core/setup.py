"""Warning: This setup.py is only there for git install until poetry support git subdirectory"""
from setuptools import setup, find_packages

setup(
    name="karrio",
    version="0.0.0-dev",
    license="LGPLv3",
    packages=find_packages(),
    install_requires=[
        "jstruct",
        "xmltodict",
        "lxml",
        "lxml-stubs",
        "py-soap",
        "Pillow",
        "phonenumbers",
        "python-barcode",
    ],
    zip_safe=False,
)
