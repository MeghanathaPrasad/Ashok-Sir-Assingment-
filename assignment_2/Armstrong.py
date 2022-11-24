n = int(input("enter the number:"))
sum = 0
p = 0
t = n 
while t>0:
    p +=1
    t //= 10
t = n
while t>0:
    r = t%10
    sum = sum+r**p
    t //=10
if sum == n:
    print("the enter number is Armstrong number")
else:
    print("this number is not a Armstrong number")
