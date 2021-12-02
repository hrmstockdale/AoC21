import pytest

from . import solution2


@pytest.fixture
def cmds():
    yield ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_solution2(cmds):
    assert solution2.solver(cmds) == 900
