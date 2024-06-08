"""Python Program to count no of even and odd numbers in the given range .
if number is divisible by 2 then even else it id odd ,we will use for loop for this 
"""
#PRAGYA MISHRA 0801IT221158
#taking range from user
lower = int(input("Enter lower range : "))
upper = int(input("Enter upper range : "))
even=0
odd=0
for i in range(lower,upper):
    if(i % 2 == 0):
        even+=1
    else:
         odd+=1
print("Number of even numbers is ",even)
print("Number of odd numbers is : ",odd)
