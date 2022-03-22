"""
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the 
digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
"""

def is_lucky(n):
    """
    Given a ticket number n, determine if it's lucky or not. 
    A ticket number is considered lucky if the sum of the first half of the 
    digits is equal to the sum of the second half.
    """
    n=str(n)
    first_half=sum([int(i) for i in n[:len(n)//2]])
    second_half=sum([int(i) for i in n[len(n)//2:]])
    return first_half==second_half

"""
process explanation for first_attempt_solution
"""

def is_lucky(n):
    """
    Given a ticket number n, determine if it's lucky or not. 
    A ticket number is considered lucky if the sum of the first half of the 
    digits is equal to the sum of the second half.
    """
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))

"""
process explanation for after_google_solution
"""