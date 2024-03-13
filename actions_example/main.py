import os

import numpy as np


def inter_quartile_range(arr: np.ndarray):
    q25 = np.quantile(arr, 0.25)
    q75 = np.quantile(arr, 0.75)
    return q75 - q25


if __name__ == "__main__":
    password = os.environ["MY_PASSWORD"]
    print(f"Your top secret password is: '{password}'.")
