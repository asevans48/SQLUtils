import os
from setuptools import setup

README = """
SI SQL Utilities

Use at your own risk under Apache v2

Utilities for creating tables, storing fields; etc.

"""

setup(
    name = "SQL Utilities",
    version = "0.0.1",
    author = "Andrew Evans",
    author_email = "aevans48@simplrinsites.com",
    description = ("PostgreSQL utilities"),
    license = "Apache v2",
    keywords = "postgresql sql psycopg2 schema tables",
    packages=['sql',],
    long_description=README,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
    ],
)