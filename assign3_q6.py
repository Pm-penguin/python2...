"""program to make a change in question 5 such yhat list become mutable and can be change. 
And this can be done by changing datatype from tuple to list."""
#PRAGYA MISHRA 0801IT221158
#taking numbers b\w 0 to 255
numbers=list(range(45,55))
#printing original list
print("Original tuple of numbers:", tuple(numbers))
# Changing the 5th and 6th elements of the list
numbers[4] = 200  # Changing the 5th element
numbers[5] = 100  # Changing the 6th element
# Print the modified list
print("Modified list of numbers:", numbers)