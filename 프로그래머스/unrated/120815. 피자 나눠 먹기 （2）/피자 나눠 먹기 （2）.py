PIZZA_SIZE = 6

def solution(n):
    for i in range(max(n, PIZZA_SIZE), n * PIZZA_SIZE + 1):
        if i % n == 0 and i % PIZZA_SIZE == 0:
            return i // PIZZA_SIZE