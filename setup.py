# Third party modules
from setuptools import setup

setup(
    install_requires=["click", "imageio", "scipy", "numpy", "pillow", "six"],
    extras_require={
        "all": ["tensorflow", "tflearn", "sklearn", "keras", "matplotlib"],
    },
)
