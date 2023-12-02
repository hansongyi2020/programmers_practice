from functools import reduce

def solution(numbers):
    sorted_list = sorted(numbers)
    return sorted_list[-2] * sorted_list[-1]