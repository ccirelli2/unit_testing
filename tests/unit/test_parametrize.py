import logging

import pandas as pd
import pytest

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(name="fix1", params=[[{}]])
def fixture_fix1(request):
    return pd.DataFrame(request.param)


@pytest.fixture(name="fix2", params=[[{}]])
def fixture_fix2(request):
    return pd.DataFrame(request.param)


def test_1(fix1):
    assert isinstance(fix1, pd.DataFrame), 'test1 failed'


def test_2(fix1, fix2):
    assert isinstance(fix1, pd.DataFrame), 'test1 failed'
    assert isinstance(fix2, pd.DataFrame), 'test2 failed'


@pytest.mark.parametrize(
    ("test_data",),
    (([{}],), ([{}],)),
    ids=["Testing some data 1", "Testing some data 2"]
)
def test3(test_data):
    assert isinstance(test_data, list), 'test3 failed'


@pytest.mark.parametrize(
    ("fix1", "fix2"),
    (
        ([{"crap1": 1}], [{"crap2": 2}]),
        ([{"crap3": 3}], [{"crap4": 4}]),
    ),

    indirect=("fix1", "fix2"),
    ids=["Testing fix1 another way", "Testing fix2 another way"]
)
def test4(fix1, fix2):
    assert isinstance(fix1, pd.DataFrame), 'test4 failed 1'
    assert isinstance(fix2, pd.DataFrame), 'test4 failed 2'
