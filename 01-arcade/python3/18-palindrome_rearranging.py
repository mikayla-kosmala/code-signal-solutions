"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example
    For inputString = "aabb", the output should be
    solution(inputString) = true.

    We can rearrange "aabb" to make "abba", which is a palindrome.
"""

def palindrome_rearranging(inputString):
    """
    Given a string, find out if its characters can be rearranged to form a palindrome.
    """
    palindrome=True
    count=0
    # Odd or Even String Length
    if len(inputString)%2==0:
        all_even=True
    else:
        all_even=False

    for i in set(inputString):
        # even length
        if inputString.count(i)%2!=0 and all_even:
            return False
        # odd length
        elif inputString.count(i)%2!=0 and not all_even:
            count+=1
            # keeping track of the number of characters
            if count>1:
                return False
    return palindrome

"""
process explanation for first_attempt_solution

If the string is odd then make sure that there is only one or zero characters that show up an odd number of times. 
Otherwise make sure there are none.

I have a count to keep track of how many characters show up an odd number of times.
"""

def palindrome_rearranging(inputString):
    """
    Given a string, find out if its characters can be rearranged to form a palindrome.
    """
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

"""
process explanation for after_google_solution:

Seems like I didn't need to worry about the length of the actual string. That
I really only needed to worry about if there are more than 1 element in the string that has an odd number.

I was thinking the case of when the string is even but there is a character that shows up an odd number 
of times, but looking at an example I realize that the string will be odd length or have two characters shown an odd number of times.
"""