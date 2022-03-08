"""
Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. 
An n-interesting polygon is obtained by taking the n - 1-interesting polygon 
and appending 1-interesting polygons to its rim, side by side. 

For n = 2, the output should be shape_area(n) = 5
For n = 3, the output should be shape_area(n) = 13.
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

def shape_area(n):
    """ 
    Your task is to find the area of a polygon for a given n.
        An n-interesting polygon is obtained by taking the n - 1-interesting polygon 
            and appending 1-interesting polygons to its rim, side by side. 
    """
    return 2*((n-1)*n) +1

"""
For this answer I knew there was a pattern to solve this solution and will try to best explain how I 
went about to the solution. I saw the pattern and thought of 4s as it is shown in the table below
+---+------+------------------------------+
| n | area | difference between n and n-1 |
+---+------+------------------------------+
| 1 |    1 |                              |
| 2 |    5 |                            4 |
| 3 |   13 |                            8 |
| 4 |   25 |                           12 |
| 5 |   41 |                           16 |
| 6 |   61 |                           20 |
+---+------+------------------------------+

It took me a while to see the patten, but there was a pattern of summing of all the values
 between 1 and n-1 then multiplying by 4 and adding 1. 

Giving me 4((n-1)(n)/2)+1 which reduced down gives me (2(n-1)(n)) + 1
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
