def solution(*num):
    for n in num:
        validateRange(n)
        
    answer = int(num[0] / num[1] * 1000)
    
    return answer

def validateRange(num):
    print("1 ~ 100 범위를 벗어났습니다.")