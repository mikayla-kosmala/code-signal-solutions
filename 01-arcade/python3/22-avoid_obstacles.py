"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example
    For inputArray = [5, 3, 6, 7, 9], the output should be
    solution(inputArray) = 4.
"""

def avoid_obstacles(inputArray):
    """
    Find the minimal length of the jump enough to avoid all the obstacles.
    """
    finding_jump_length = True
    count=2
    while finding_jump_length:
        for i in inputArray:
            if i%count==0:
                count+=1
                finding_jump_length=True
                break
            else:
                finding_jump_length=False
                continue
    return count


"""
process explanation for first_attempt_solution

"""

def avoid_obstacles(inputArray):
    """
    Find the minimal length of the jump enough to avoid all the obstacles.
    """
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1
"""
process explanation for after_google_solution:

why hello little all() function who are you and what do you do?

The all() function is an inbuilt function in python which returns true if all the
elements of a given iterable are True else it returns False

isdigit() method returns True if all the characters are digits, otherwise false
"""