#HW 3
#Due Date: 02/01/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave assistance
#
########################################
def findNextOpr(txt):
    if not isinstance(txt, str) or len(txt) <= 0:
        return "error: findNextOpr"
    # Checks for the position of the first operator in a text and returns the position value
    for i in range(len(txt)):
        if txt[i] == '*' or txt[i] == '+' or txt[i] == '-' or txt[i] == '/' or txt[i] == '^':
            return i
    return -1


def isNumber(txt):
    if not isinstance(txt, str) or len(txt) == 0:
        return "error: isNumber"
    # Test to see if it can be converted to a number
    try:
        if float(txt):
            return True
    except ValueError:
        return False



def getNextNumber(expr, pos):
    if not isinstance(expr, str) or not isinstance(pos, int) or len(expr) == 0 or pos < 0 or pos >= len(expr):
        return None, None, "error: getNextNumber"
    expr = expr[pos:]
    # Check to see if the string is simply a number with no operators
    if isNumber(expr):
        return (float(expr), None, None)
    # Find the operator and if there is none, set both operator and position to None
    opPos = findNextOpr(expr)
    if opPos < 0:
        op = None
        opPos = None
    else:
        # Define the operator if it exists
        op = expr[opPos]
        # Check if there is a number before the -
        # If there isn't then the first number is a negative
        if op == '-' and (opPos == 0 or not isNumber(expr[:opPos])):
            secondOp = findNextOpr(expr[opPos+1:]) + opPos + 1
            num = float("".join(expr[opPos:secondOp].split()))
            op = expr[secondOp]
            opPos = pos + secondOp
            return (num, op, opPos)
        expr = expr[:opPos]
        opPos += pos
    # If there is no number after the operator, just return the operator and its position
    if len(expr) == 0:
        return(None, op, opPos)
    # Otherwise just push the number with the operators
    if isNumber(expr):
        num = float(expr)
    else:
        num = None
    return (num, op, opPos)

