#Let's calculate the mode of serie

from collections import Counter


def Mode(X):
    frequencies = Counter(X)
    maximumFrequency = max(frequencies.values())
    return [value for value in X if frequencies[value] == maximumFrequency]

    
        
    