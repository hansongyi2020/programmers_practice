PIZZA_SIZE = 7

def solution(n):
    result = divmod(n, PIZZA_SIZE)
    return result[0] + 1 if result[1] else result[0]