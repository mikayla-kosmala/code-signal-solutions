"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def common_character_count(s1,s2):
    """
    Given two strings, find the number of common characters between them.
    """
    count=0
    s2 = [i for i in s2]
    for i in s1:
        if i in s2:
            count+=1
            s2.remove(i)
    return count

"""
process explanation for first_attempt_solution
"""

def common_character_count(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)

"""
process explanation for after_google_solution
"""