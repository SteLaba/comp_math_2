import numpy as np
from matplotlib import pyplot as plt


def draw(f, a: int, b: int):
    x = np.arange(a, b, 0.1)
    fun = np.vectorize(f)
    plt.plot(x, fun(x))
    plt.plot(x, 0 * x)
    plt.show()
