"""Python program to multiply two lists."""
#PRAGYA MISHRA 0801IT221158
#given list
A = [1,4,5,7,3]
B = [2,0,8,-3]
product = [a * b for a, b in zip(A, B)]
print("Result of multiplying corresponding elements:", product )
