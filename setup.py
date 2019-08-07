#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Setup script for the `kiara`-package."""

import inspect
import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

__location__ = os.path.join(
    os.getcwd(),
    os.path.dirname(inspect.getfile(inspect.currentframe()))
)


def read_version(package):
    """Reads version from provided package.

    Arguments:
        package - str(): package name

    Returns str() with version."""
    with open(os.path.join(package, "__init__.py"), "r") as file_handle:
        for line in file_handle:
            if line.startswith("__version__ = "):
                return line.split()[-1].strip().strip("\"")
    return None


def readme():
    """Returns str() with package documentation."""
    try:
        return open('README.rst', encoding='utf-8').read()
    except TypeError:
        return open('README.rst').read()


VERSION = read_version("blackjack")

INSTALL_REQUIRES = [
    "setuptools>=5.5.1"
]

TESTS_REQUIRE = [
    "flake8>=3.4.0",
    "isort>=4.3.4",
    "pytest>=3.6.1",
    "pytest-cov>=2.5.1",
    "pycodestyle>=2.3.1",
    "pylint>=1.9.2"
]


class PyTest(TestCommand):
    """Initializes test suite."""

    user_options = [("cov-html=", None, "Generate junit html report")]

    def initialize_options(self):
        # pylint: disable=attribute-defined-outside-init

        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = [
            "--cov",
            "blackjack",
            "--cov-report",
            "term-missing",
            "-v"
        ]

        self.cov_html = False

    def finalize_options(self):
        TestCommand.finalize_options(self)

        if self.cov_html:
            self.pytest_args.extend(["--cov-report", "html"])

        self.pytest_args.extend(["tests"])

    def run_tests(self):
        import pytest

        sys.exit(pytest.main(self.pytest_args))


setup(
    name="blackjack",
    version=VERSION,
    author="Léon Spaans",
    author_email="leons [at] gridpoint <dot> nl",
    maintainer="Léon Spaans",
    maintainer_email="leons [at] gridpoint <dot> nl",
    description=(
        "A Blackjack simulator"
    ),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "test": TESTS_REQUIRE
    },
    cmdclass={'test': PyTest},
    test_suite='tests',
    keywords="python blackjack",
    url="https://github.com/lspaans/blackjack.git",
    packages=find_packages(),
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ],
    zip_safe=False
)
