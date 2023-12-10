def solution(my_string):
    vowel = "aeiou"
    return ''.join(i for i in my_string if i not in vowel)