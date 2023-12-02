from functools import reduce

def solution(numbers):
    sorted_list = sorted(numbers)
    return reduce(lambda x, y: x * y, sorted_list[-2:])