from math import prod

def solution(box, n):
    return prod([inch // n for inch in box])