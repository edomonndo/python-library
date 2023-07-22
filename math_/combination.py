
import math
def comb(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))