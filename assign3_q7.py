""" 
Check whether a number is in the range (1000, 10000) or not.
"""
#PRAGYA MISHRA 0801IT221158
# taking input from the user
num = int(input("Enter a number to check if it's in the range (1000, 10000): "))

# checking if the number is in the range
if 1000 < num < 10000:
    print("The number is in the range (1000, 10000).")
else:
    print("The number is NOT in the range (1000, 10000).")
