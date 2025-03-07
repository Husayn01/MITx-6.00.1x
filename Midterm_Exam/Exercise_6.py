# Write a function called general_poly, that meets the specifications below. 
# For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because .

# def general_poly (L):
#     """ L, a list of numbers (n0, n1, n2, ... nk)
#     Returns a function, which when applied to a value x, returns the value 
#     n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
#     #YOUR CODE HERE

def general_poly(L):
    """ 
    L: a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... + nk * x^0
    """
    def func(x):
        result = L[0]
        for y in L[1:]:
            result = result * x + y
        return result
    return func
