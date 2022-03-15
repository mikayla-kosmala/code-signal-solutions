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

def make_array_consecutive_2(sequence):
    """ 
    Return True if the following list be strictly increasing if one element is removed. Else False.
    """
    output_list=[]
    for i in range(len(sequence)+1):
        new_sequence = sequence[:i-1]+sequence[i:]
        print(new_sequence)
        output=True
        for j in range(len(new_sequence)-1):
            output = output and new_sequence[j] < new_sequence[j+1]
        output_list.append(output)
    return len(set(output_list))==2

"""
The function above worked for all the free tests, but exceded the time limit exceeded for the hidden tests
which means we need to computationally improve our formula. I couldn't think of a way to do it without googling.

The idea behind this was to remove each element in the list and then check to see if it is strictly asscending
To see 
"""

def make_array_consecutive_2(sequence):
    """ 
    function description
    """
    for i in range(len(sequence)):
        element = sequence.pop(i)
        if sequence == sorted(sequence):
            return True
        sequence.insert(i,element)
    return False

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

array_ = [1,3,2]

print(make_array_consecutive_2(array_))