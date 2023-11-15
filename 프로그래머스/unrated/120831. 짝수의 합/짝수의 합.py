def solution(n):
    validateRange(n)
    
    return sum([i for i in range(2, n + 1, 2)])

def validateRange(n):
    if (n < 1 and n > 1000):
        print("1 ~ 1000 범위를 벗어났습니다.")