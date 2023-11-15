def solution(age):
    validateAge(age)
    
    measure_age = 1
    measure_year = 2022

    return measure_year - (age - measure_age)

def validateAge(age):
    if(age < 1 and age > 120):
        print("1 ~ 120 입력 범위를 벗어났습니다.")