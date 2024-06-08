"""Python prgram to print pascal's triangle for row 5 ."""
#PRAGYA MISHRA 0801IT221158
# Print Pascal's Triangle in Python
from math import factorial
# input n
n = 5
for i in range(n):
    for j in range(n-i+1):
        # for space 
        print(end=" ")
    for j in range(i+1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    # for new line
    print()