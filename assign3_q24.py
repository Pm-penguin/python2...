"""Python program to change a element of tuple.
First we will convert tuple into list and then changes can be made . """
#PRAGYA MISHRA 0801IT221158
# Create the tuple with 15 elements
x = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
y=list(x)
y[2]="Python"
x_change=tuple(y)
print(x_change)
