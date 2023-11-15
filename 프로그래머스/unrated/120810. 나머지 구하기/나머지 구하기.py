def solution(num1, num2):
    validate(num1)
    validate(num2)
    
    answer = num1 % num2
    return answer

def validate(num):
    if(num < 1 and num > 100):
        print("1 ~ 100 범위를 벗어났습니다.")