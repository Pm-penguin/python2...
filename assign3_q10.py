"""Python program to reverse a number .
We will a while loop for geting result.
"""
#PRAGYA MISHRA 0801IT221158
#taking input
num = int(input("Enter the positive number to be reversed:"))
rev=0
if(num>0):
    while(num!=0):
        digit=num%10
        rev=rev*10+digit
        num//=10
else:
    print("Not a positive number. ")        
print("Reversed number :",rev)
