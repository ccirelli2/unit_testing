import os
import sys
import pandas as pd
import logging
import pytest

logging.basicConfig(level=logging.DEBUG)


# Fixtures
@pytest.fixture
def fix1():
    return pd.DataFrame({})


@pytest.fixture
def fix2():
    return pd.DataFrame({})


# Tests
def test1(fix1, ids=['fix1']):
    assert isinstance(fix1, pd.DataFrame), 'test1 failed'

def test2(fix1, fix2, ids=['fix1', 'fix2']):
    assert isinstance(fix1, pd.DataFrame), 'test1 failed'
    assert isinstance(fix2, pd.DataFrame), 'test2 failed'

@pytest.mark.xfail
@pytest.mark.parametrize("test_data", ["fix1", "fix2"], ids=["fix1", "fix2"])
def test3(test_data):
    assert isinstance(test_data, pd.DataFrame), 'test3 failed'


@pytest.mark.parametrize("test_data", ["fix1", "fix2"], ids=["fix1", "fix2"])
def test4(test_data, request):
    data = request.getfixturevalue(test_data)
    assert isinstance(data, pd.DataFrame), 'test4 failed'

