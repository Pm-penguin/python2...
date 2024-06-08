"""Python Program to exchange the values of two numbers."""
#PRAGYA MISHRA 0801IT221158
#taking input
a = int(input("First number:"))
b = int(input("Second number:"))
print("Numbers after exchanging the values:")
#exchanging the values
temp = a
a = b
b = temp
#printing
print("First number:",a)
print("Second number:",b)