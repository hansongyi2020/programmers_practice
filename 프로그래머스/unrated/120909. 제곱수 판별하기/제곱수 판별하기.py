def solution(n):
    square = [i *i for i in range(1, 1000 + 1)]
    return 1 if n in square else 2