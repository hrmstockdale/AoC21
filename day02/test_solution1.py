import pytest

from . import solution1


@pytest.fixture
def cmds():
    yield ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_solution1(cmds):
    assert solution1.solver(cmds) == 150
