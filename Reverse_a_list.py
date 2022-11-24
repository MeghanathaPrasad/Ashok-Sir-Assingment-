
from operator import truediv

ele = int(input("how many elements have to add in list: "))
l=[]
for i in range(ele):
    e = int(input("add element:"))
    l.append(e)

print("Finally your list is: ",l)
print("Your Reversed list is: ",l[::-1])
# L=[1,2,3,4,5,6,7,8,9,10]
# L2 = L[::-1]
# print(L2)

