import random
from collections import Counter


def generateRandomResult():
    return random.randint(1, 6)


def generateRandomResults(n):
    return [generateRandomResult() for _ in range(n)]


print(Counter(generateRandomResults(20000)))
