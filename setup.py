from setuptools import setup

setup(
    name="IexCli",
    version="1.0",
    py_modules=["iex", "functions"],
    install_requires=[
        "Click", "requests"
    ],
    entry_points='''
        [console_scripts]
        iex=iex:cli
    ''',
)