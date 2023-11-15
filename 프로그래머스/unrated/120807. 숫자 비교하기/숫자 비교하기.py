def solution(num1, num2):
    validateRange(num1)
    validateRange(num2)
    
    if (num1 == num2):
        return 1
    return -1

def validateRange(num):
    if (num < 0 and num > 10000):
        print("0 ~ 10000 범위를 벗어났습니다.")