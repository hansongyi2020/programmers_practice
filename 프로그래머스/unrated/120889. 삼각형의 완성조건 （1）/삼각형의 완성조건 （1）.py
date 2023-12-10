def solution(sides):
    sorted_list = sorted(sides)
    return 1 if(sorted_list[0] + sorted_list[1] > sorted_list[2]) else 2