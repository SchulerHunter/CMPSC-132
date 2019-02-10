#Lab #8
#Due Date: 02/22/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: I neither sought nor gave assistance
#
########################################
def isPrime(n, i = 2):
    # i is a preloaded divisor
    '''
    >>> isPrime(5)
    True
    >>> isPrime(1)
    False
    >>> isPrime(9)
    False
    >>> isPrime(85)
    False
    >>> isPrime(1019)
    True
    >>> isPrime(2)
    True
    >>> isPrime(0)
    False
    '''
    # If n is 0 or 1, return false
    if n < 2:
        return False
    if n == 2:
        return True
    # If n is evenly divisible by the divisor, return false
    if n % i == 0:
        return False
    # If i^2 is greater than n, it must be a prime number
    if n < i**2:
        return True
    # Recursively increase i
    return isPrime(n, i+1)
