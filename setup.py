from setuptools import setup

setup(
    name="cgit",
    version="1.0",
    packages=["cgit"],
    entry_points={"console_scripts": ["cgit = cli:main"]},
)
