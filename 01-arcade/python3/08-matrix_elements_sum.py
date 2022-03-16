"""
After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a rumour 
that all the free rooms are haunted! Since the CodeBots are quite superstitious, they 
refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost 
of the room, your task is to return the total sum of all rooms that are suitable for 
the CodeBots (ie: add up all the values that don't appear below a 0).

Example:
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

results -> 1 + 5 + 1 + 2 = 9.
"""

def matrix_elements_sum(matrix):
    """
    Given matrix, a rectangular matrix of integers, where each value represents 
    the cost of the room, your task is to return the total sum of all rooms that
    are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
    """
    suitable_cols=[]
    count=0
    for i in range(len(matrix[0])):
        if matrix[0][i]!=0:
            suitable_cols.append(i)
            count+=matrix[0][i]
    print(suitable_cols)
    for j in suitable_cols:
        print('suitable',j)
        for k in range(1,len(matrix)):
            print('row',k)
            print("hi",matrix[k][j])
            if matrix[k][j]!=0:
                count+=matrix[k][j]
            else:
                print('removing',j)
                break
    return count

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