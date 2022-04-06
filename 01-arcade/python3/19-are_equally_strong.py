"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example
    For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
    solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
    For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
    solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
    For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
    solution(yourLeft, yourRight, friendsLeft, friendsRight) = false.
"""

def are_equally_strong(yourLeft, yourRight, friendsLeft, friendsRight):
    """
    Call two arms equally strong if the heaviest weights they each are able to lift are equal.

    Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

    Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
    """
    
    return max([yourLeft,yourRight]) == max([friendsLeft,friendsRight]) and min([yourLeft,yourRight]) == min([friendsLeft,friendsRight])

"""
process explanation for first_attempt_solution

If the mins and max of your arm and friends arm are the same then we are good... Boom
"""

def are_equally_strong(yourLeft, yourRight, friendsLeft, friendsRight):
    """
    Call two arms equally strong if the heaviest weights they each are able to lift are equal.

    Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

    Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
    """
    
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}

"""
process explanation for after_google_solution:

Grrrrr sets is a way smarter move to the solution.
"""