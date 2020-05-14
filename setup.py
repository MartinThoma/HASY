from setuptools import setup


setup(
    package_data={"hasy": ["data/currencies.csv"]},
    install_requires=["click"],
    extras_require={"all": ["tensorflow", "tflearn", "sklearn", "keras", "matplotlib"],},
)
