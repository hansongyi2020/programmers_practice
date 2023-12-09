def solution(array):
    frequency = {}
    for i in array:
        try:
            frequency[i] += 1
        except KeyError:
            frequency[i] = 1

    sorted_list = sorted(frequency.values())
    if sorted_list.count(sorted_list[-1]) == 1:
        for k, v in frequency.items():
            if v == sorted_list[-1]:
                return k
    return -1