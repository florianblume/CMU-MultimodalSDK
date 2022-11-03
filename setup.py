import os
import logging

from importlib.machinery import SourceFileLoader
from setuptools import setup, find_packages

version = (
    SourceFileLoader("mmsdk.version", os.path.join("mmsdk", "version.py")).load_module().VERSION
)

setup(
    name="mmsdk",
    version=version,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=['h5py', 'validators', 'tqdm', 'numpy', 'argparse', 'requests'],
    zip_safe=False,
    author="Amir Zedah",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords="multi-modal dataset machine learning",
    url="https://github.com/A2Zadeh/CMU-MultimodalSDK",
    python_requires=">=3.6",
    project_urls={
        "Source Code": "https://github.com/A2Zadeh/CMU-MultimodalSDK",
    },
)
