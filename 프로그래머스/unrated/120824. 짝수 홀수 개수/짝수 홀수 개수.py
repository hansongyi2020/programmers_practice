def solution(num_list):
    result_list = [0, 0]
    for num in num_list:
        if num % 2 == 0:
            result_list[0] += 1
        else:
            result_list[1] += 1
    return result_list