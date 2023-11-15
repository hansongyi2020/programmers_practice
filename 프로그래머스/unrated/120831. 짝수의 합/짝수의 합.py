def solution(n):
    validateRange(n)
    
    answer = 0
    for i in range(2, n + 1, 2): 
            answer += i
    return answer

def validateRange(n):
    if (n < 1 and n > 1000):
        print("1 ~ 1000 범위를 벗어났습니다.")