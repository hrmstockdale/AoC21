from . import solution1


def test_solver_counts_depth_increases():
    assert solution1.solver(["1", "2", "3", "2", "1", "2"]) == 3
