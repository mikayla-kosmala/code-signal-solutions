"""
Some people are standing in a row in a park. There are trees between
them which cannot be moved. Your task is to rearrange the people by
their heights in a non-descending order without moving the trees.
People can be very tall!
"""

def sort_by_height(a):
    """
    Rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!
    """
    people = sorted([i for i in a if i!=-1])
    for i in range(len(a)):
        if a[i]!=-1:
            a[i]=people.pop(0)
    return a

"""
process explanation for first_attempt_solution
"""

def sort_by_height(a):
    """
    Rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!
    """
    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l

"""
process explanation for after_google_solution
"""