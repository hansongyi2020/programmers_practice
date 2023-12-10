def solution(*num):
    for n in num:
        validateRange(n)
    
    answer = sum(num)
    return answer

def validateRange(num):
    if (num < -50000 and num > 50000):
        print("-50000 ~ 50000 범위를 벗어났습니다.")