"""
Given an array of integers, find the pair of adjacent elements that has the
 largest product and return that product.

 Example:
 For inputArray = [3, 6, -2, -5, 7, 3], the output should be
    solution(inputArray) = 21.

 7 and 3 produce the largest product.
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

def adjacent_element_product(inputArray):
    """ 
    function description
    """
    max = inputArray[0]*inputArray[1]
    for i in range(len(inputArray)-1):
        if inputArray[i]*inputArray[i+1] >max:
            max = inputArray[i]*inputArray[i+1] 
    return max

"""
I am a for/while loop main. For loops made so much sense to me when I was starting to learn
python. Sadly it isn't as computationally friendly, but this is the first go at this problem. 
In the first attempt I set the max to be the product of the first and second element of the list.
I then loop through the array to see if there are any adjacent elements that have a larger product than the max
 (if inputArray[i]*inputArray[i+1] >max:). If true then reset max to be that larger product and once 
we are done iterating through each element in the list then we return max.
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
