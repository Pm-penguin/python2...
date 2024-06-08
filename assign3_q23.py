"""Find the output."""
#PRAGYA MISHRA 0801IT221158
list1 = [2, 3, [4, 5]]
 # shallow copy
list2 = list1.copy() 
# modify the first element of list2
list2[0] = 88
# print list1
print("Original list1:", list1)
# print list2
print("Modified list2:", list2)
