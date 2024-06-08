"""Program to replace list values inside a tuple."""
#PRAGYA MISHRA 0801IT221158
# Define the original tuple with lists as elements
tuple1 = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
# Display the original tuple
print("Original Tuple:", tuple1)
# Replace the second list with a new list
lis = [10, 11, 12]
list1=list(tuple1)
list1[1]=lis
tuple2=tuple(list1)
print("New Tuple :",tuple2)

