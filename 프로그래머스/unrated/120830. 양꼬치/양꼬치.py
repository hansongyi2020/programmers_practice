SKEWER_PRICE = 12000
BEVERAGE_PRICE = 2000

def solution(n, k):
    validateSkewer(n)
    validateBeverage(n, k)

    answer = SKEWER_PRICE * n + BEVERAGE_PRICE * (k - n // 10)
    
    return answer

def validateSkewer(n):
    if (n < 1 and n > 999):
        print("1 ~ 999 범위를 벗어났습니다.")
        
def validateBeverage(n, k):
    if (k < n / 10 and k > 999):
        print("{0} ~ 999 범위를 벗어났습니다.".format(n / 10))