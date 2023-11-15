def solution(num1: int, num2: int) -> int:
    validateRange(num1)
    validateRange(num2)
    
    answer = num1 // num2
    return answer

def validateRange(num):
    if(num < 1 and num > 100):
        print("1 ~ 100 범위를 벗어났습니다.")