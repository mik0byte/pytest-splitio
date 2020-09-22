# -*- coding: utf-8 -*-

import os
import pytest
from .split_client import SplitClient

split_client = SplitClient()


def pytest_sessionstart(session):
    global split_client
    split_sdk_key = os.environ.get("SPLIT_KEY")
    if session.config.getoption("SPLIT_KEY") or split_sdk_key:
        split_client.init_client(split_sdk_key=split_sdk_key or session.config.getoption("SPLIT_KEY"))


def pytest_addoption(parser):
    group = parser.getgroup('split')
    group.addoption(
        '--SPLIT-KEY',
        action='store',
        help='Set the value for the Split SDK key.'
    )


def pytest_configure(config):
    config.addinivalue_line("markers",
                            "skipif_split_equals(split, treatment): "
                            "This mark skips the test if the given split is equal to the given treatment")
    config.addinivalue_line("markers",
                            "skipif_split_not_equal(split, treatment): "
                            "This mark skips the test if the given split is not equal to the given treatment")


def pytest_runtest_setup(item):
    global split_client

    if split_client.status:
        skipif_split_equals_arguments = [mark.args for mark in item.iter_markers(name="skipif_split_equals")]
        skipif_split_not_equals_argument = [mark.args for mark in item.iter_markers(name="skipif_split_not_equal")]

        if skipif_split_equals_arguments:
            try:
                split_name, treatment = skipif_split_equals_arguments[0]
            except ValueError:
                raise ValueError("More than two arguments provided for skipif_split_equals marker")
            if split_name and treatment:
                server_treatment = split_client.get_treatment(split_name)
                if server_treatment == treatment:
                    pytest.skip(f"Test skipped because '{split_name} == {treatment}' condition is false")

        if skipif_split_not_equals_argument:
            try:
                split_name, treatment = skipif_split_not_equals_argument[0]
            except ValueError:
                raise ValueError("More than two arguments provided for skipif_split_not_equals marker")
            if split_name and treatment:
                server_treatment = split_client.get_treatment(split_name)
                if server_treatment != treatment:
                    pytest.skip(f"Test skipped because '{split_name} != {treatment}' condition is false")


@pytest.fixture
def split():
    global split_client

    if split_client.status:
        return split_client
