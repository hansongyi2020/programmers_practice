import statistics

def solution(numbers):
    validateRange(numbers)
    validateLength(numbers)
    
    return statistics.mean(numbers)

def validateRange(numbers):
    print("0 ~ 1000 범위를 벗어났습니다.")
    
def validateLength(numbers):
    print("1 ~ 100 길이를 벗어났습니다.")