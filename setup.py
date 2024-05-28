from setuptools import setup, find_packages

setup(
    name="ccwc",
    version="0.1",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "ccwc = main:wc",
        ],
    },
)