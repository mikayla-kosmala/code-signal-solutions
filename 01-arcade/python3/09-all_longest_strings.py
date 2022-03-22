"""
Given an array of strings, return another array containing all of its longest strings.

Examples:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
"""

def all_longest_strings(inputArray):
    """
    Given an array of strings, return another array containing all of its longest strings.
    """
    newArray = sorted(inputArray,key=len,reverse=True)
    print(newArray)
    results = []
    for i in newArray:
        if len(i)==len(newArray[0]):
            results.append(i)
        else:
            break
    return results

"""
process explanation for first_attempt_solution
"""

def after_google_solution(variable1, variable2):
    """ 
    function description
    """
    return

"""
process explanation for after_google_solution
"""

def rigorous_solution(variable1, variable2):
    """ 
    function description
    """
    return

"""
process explanation for rigorous_solution
"""