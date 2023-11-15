def solution(angle):
    validateAngle(angle)
    
    if (0 < angle < 90):
        return 1
    if (angle == 90):
        return 2
    if (90 < angle < 180):
        return 3
    if (angle == 180):
        return 4

def validateAngle(angle):
    if (angle < 1 and angle > 180):
        print("1 ~ 180 범위를 벗어났습니다.")