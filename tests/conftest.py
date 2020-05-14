"""Configure pytest."""

# Core Library modules
import logging


def pytest_configure(config):
    """Flake8 is to verbose. Mute it."""
    logging.getLogger("flake8").setLevel(logging.WARN)
    logging.getLogger("pydocstyle").setLevel(logging.INFO)
