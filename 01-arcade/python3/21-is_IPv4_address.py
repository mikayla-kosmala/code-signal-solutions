"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example
    For inputString = "172.16.254.1", the output should be
    solution(inputString) = true;

    For inputString = "172.316.254.1", the output should be
    solution(inputString) = false.
    316 is not in range [0, 255].

    For inputString = ".254.255.0", the output should be
    solution(inputString) = false.
    There is no first number.
"""

def is_IPv4_address(inputString):
    """
    Given a string, find out if it satisfies the IPv4 address naming rules.
    """
    try:
        return sum([int(i)>=0 and int(i)<=255 if i!='' and not (i[0]=='0' and len(i)>1) else False for i in inputString.split('.')])==4 and len(inputString.split('.'))==4
    except:
        return False


"""
process explanation for first_attempt_solution

"""

def is_IPv4_address(inputString):
    """
    Given a string, find out if it satisfies the IPv4 address naming rules.
    """
    p = inputString.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)
"""
process explanation for after_google_solution:

why hello little all() function who are you and what do you do?

The all() function is an inbuilt function in python which returns true if all the
elements of a given iterable are True else it returns False

isdigit() method returns True if all the characters are digits, otherwise false
"""