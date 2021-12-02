from . import solution2


def test_solver_counts_three_depths_increases():
    assert solution2.solver(["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]) == 5