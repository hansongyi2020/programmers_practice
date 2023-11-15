def solution(num1, num2):
    validateRange(num1)
    validateRange(num2)
    
    answer = num1 * num2
    return answer

def validateRange(num):
    if (num < 0 and num > 100):
        print("0 ~ 100 범위를 벗어났습니다.")