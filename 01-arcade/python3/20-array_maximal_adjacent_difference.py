"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example
    For inputArray = [2, 4, 1, 0], the output should be
    solution(inputArray) = 3.
"""

def array_maximal_adjacent_difference(inputArray):
    """
    Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
    """ 
    return max([abs(inputArray[i]-inputArray[i+1]) for i in range(len(inputArray)-1)])

"""
process explanation for first_attempt_solution

"""

"""
process explanation for after_google_solution:

Same as the first attempt solution
"""