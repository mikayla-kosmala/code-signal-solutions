"""
Write a function that reverses characters in (possibly nested) 
parentheses in the input string.

Input strings will always be well-formed with matching ()s.
"""

def are_similar(a, b):
    """
    Two arrays are called similar if one can be obtained from another 
    by swapping at most one pair of elements in one of the arrays.
    """
    if a==b:
        return True
    elif set(a)!=set(b):
        return False
    else:
        for i in range(len(a)-1):
            if a[i]!=b[i]:
                for j in range(i+1,len(a)):
                    ai = a[i]
                    aj = a[j]
                    a[i]=aj
                    a[j]=ai
                    if a==b:
                        return True
                    else:
                        a[i]=ai
                        a[j]=aj
                return False

"""
process explanation for first_attempt_solution
"""

def are_similar(a, b):
    """
    Two arrays are called similar if one can be obtained from another 
    by swapping at most one pair of elements in one of the arrays.
    """
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2

"""
process explanation for after_google_solution
"""