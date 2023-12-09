from collections import Counter

def solution(array):
    frequency = Counter(array).most_common(2)

    if len(frequency) >= 2 and frequency[0][1] == frequency[1][1]:
            return -1
    return frequency[0][0]