import numpy as np

from actions_example.main import inter_quartile_range


def test_inter_quartile_range():
    arr = np.array([10, 11, 12, 13, 14])
    assert inter_quartile_range(arr) == 2
