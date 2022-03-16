"""
Given a sequence of integers as an array, determine whether it is possible to obtain
 a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if 
a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example:
For sequence = [1, 3, 2, 1], the output should be solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence 
[1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

# Imports that are automatically included:
import json
import math
import string
import re
import random
import sys
from tempfile import TemporaryFile
import traceback
import functools
from collections import OrderedDict

import numpy
import sortedcontainers

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
The function above worked for all the free tests, but exceded the time limit exceeded for the hidden tests
which means we need to computationally improve our formula. I couldn't think of a way to do it without googling.

The idea behind this was to remove each element in the list and then check to see if it is strictly asscending
To see 
"""

def first_bad_pair(sequence):
    """Return the first index of a pair of elements where the earlier
    element is not less than the later elements. If no such pair
    exists, return -1."""
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1
    
def almost_increasing_sequence(sequence):
    """ 
    Return True if the following list be strictly increasing if one element is removed. Else False.
    """    
    j = first_bad_pair(sequence)
    if j == -1:
        return True  # List is increasing
    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasing


"""
To save on the number of iterations we make a new function first_bad_pai
"""

def almost_increasing_sequence(sequence):
    """ 
    function description
    """
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


"""
process explanation for rigorous_solution
"""

array_ = [1,3,2]

print(make_array_consecutive_2(array_))