from enum import Enum

class Offense(Enum):
    GENERAL_ANT = 5
    SOLDIER_ANT = 3
    WORKING_ANT = 1

def solution(hp):
    count = 0
    for power in Offense:
        count += hp // power.value
        hp = hp % power.value
    return count