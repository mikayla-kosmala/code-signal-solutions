"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
each statue having an non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue will be bigger than 
the previous one exactly by 1. He may need some additional statues to be able to accomplish that. 
Help him figure out the minimum number of additional statues needed.

Example
For statues = [6, 2, 3, 8], the output should be solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
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

def make_array_consecutive_2(list_of_int):
    """ 
    Find the number of integers that need to be added to the array such that the array would contain 
    every integer from an interval [L,R] S being the smallest and L being the largest integer
    """
    min_ = min(list_of_int)
    max_ = max(list_of_int)
    return len(range(min_,max_+1)) - len(list_of_int)
    return 

"""
Good thing we are just trying to find how many need to be found to complete the array. That would of 
made this problem a bit different. Because we are only looking for how many we need to complete the 
array it means we only need to compare the length of a complete list and the list given.

For the example above the min is 2 and the max is 8, so the complete array is
[2,3,4,5,6,7,8]. What is given was [2,3,6,8]. With this information we just need to compare the lengths
to determine how many more elements would need to be added to the given array to complete it. 

How I completed the array was creating an list using range(min,max+1) 
[Reason why I need to add 1 to the max is because range doesn't include the max in the list based 
on its documentation]
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