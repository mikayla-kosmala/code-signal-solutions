"""
Given a year, return the century it is in. The first century spans from the year 1 up to
 and including the year 100, the second - from the year 101 up to and including the year 200, etc.

For year = 1905, the output should be century_from_year(year) = 20
For year = 1700, the output should be
solution(year) = 17.
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

def century_from_year(year):
    """ 
    First attempt: Given a year, return the century it is in
    """
    if year%100 == 0:
        return year//100
    else:
        return (year//100)+1

"""
Since we are trying to solve what century we are in I knew there would have to be some sort of 
division and modular involving 100. It was a bit of a trial and error. This could of been done 
in a single line, but this one my first inital test.
"""

def century_from_year(year):
    """ 
    Second Attempt: Given a year, return the century it is in
    """
    return int(-(-year // 100))

"""
I knew there had to be an easier way to solve the century_from_year while doing the first try.

This was the craziest solution I found on the internet! I was searching for how to round up 
without math.ceil() and found this solution. 

This works because integer division by 100 (and 1) rounds down, but using the negative sign before and after doing
the division rounds the opposite direction.
"""

def century_from_year(year):
    """ 
    Rigorous Solution: Given a year, return the century it is in
    -INPUT-
    year: 1 <= int <=2005
    -OUTPUT-
    int - the number of the century the year is in
    """
    try:
        return
    except:
        return 

"""
process explanation for rigorous_solution
"""