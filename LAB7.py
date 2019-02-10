#Lab #7
#Due Date: 02/22/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: I neither sought nor gave assistance
#
########################################
#### DO NOT modify the triangle(n) function in any way!
def triangle(n):
    return recursive_triangle(n, n)

###################
def recursive_triangle(k, n):
    # If the provided k is zero, return none
    if k == 0:
        return ''
    # Check if the current state is the last and don't make a recursive call
    elif k - 1 == 0:
        return((' ' * (n-k)) + ('*' * k))
    # If the current state is not the last, continue calling
    elif k - 1 != 0:
        return((' ' * (n-k)) + ('*' * k) + ('\n') + recursive_triangle(k-1,n))
    # Backup case is to return none
    else:
        return None
