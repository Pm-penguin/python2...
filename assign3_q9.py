"""Python program to give square of first five natural numbers."""
#PRAGYA MISHRA 0801IT221158
#making list
num_list = list(range(1,6))
print(num_list)
#doing square and making square list using for loop
squ_list = [i**2 for i in num_list]
print(squ_list)