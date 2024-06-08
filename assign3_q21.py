"""Python program to find greatest number in list.
by sorting list .
"""
#PRAGYA MISHRA 0801IT221158
#empty list
myList=[]
n=int(input("Enter no of elements in list:"))
for i in range(n):
    num=float(input("Enter number "+str(i+1)+":"))
    myList.append(num)
#sorting list
myList.sort()
# printing the last element
print("Largest element is:", myList[-1])
