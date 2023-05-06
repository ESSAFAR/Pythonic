import numpy as np
from collections import Counter


def generateRandomResult():
    return np.random.randint(1,7)


def generateRandomResults(n):
    return [generateRandomResult() for _ in range(n)]


X = generateRandomResults(2000000)
print(Counter(X))
