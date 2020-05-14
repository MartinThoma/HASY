# Third party modules
from setuptools import setup

setup(
    install_requires=["click"],
    extras_require={
        "all": ["tensorflow", "tflearn", "sklearn", "keras", "matplotlib"],
    },
)
