"""
Write a function that returns the sum of two numbers.

Example: For param1 = 1 and param2 = 2, the output should be
add(param1, param2) = 3.
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

def add(variable1, variable2):
    """ 
    First attempt: Adding together variable1 and variable2 with an addition sign
    """
    return variable1+variable2

"""
There isn't any different way to add numbers together unless they are in a list, set or array.
"""

def add(variable1: float, variable2: float) -> float:
    """ 
    Rigorous Attempt: Adding together variable1 and variable2 with an addition sign
    -INPUT-
    variable1: float
    variable2: float
    -OUTPUT-
    float
    """
    try:
        return variable1+variable2
    except TypeError:
        print('Oops! One of the inputs was not a valid number. Try again...')
        return

"""
Added an exception to the function to make sure that the variables being fed through the function
are floats or int. 
"""