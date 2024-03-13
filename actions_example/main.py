import numpy as np


def inter_quartile_range(arr: np.ndarray):
    q25 = np.quantile(arr, 0.25)
    q75 = np.quantile(arr, 0.75)
    return q75 + q25
