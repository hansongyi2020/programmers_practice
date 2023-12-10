def solution(my_string):
    new_string = ''
    for str in my_string:
        if str.islower():
            new_string += str.upper()
        else:
            new_string += str.lower()
    return new_string