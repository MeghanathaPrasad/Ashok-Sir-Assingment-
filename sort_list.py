# a = [1,0,-1,-2,1,-1,0]
# b=[]
# for i in a:
#     m=min(a)
#     b.append(m)
#     a.remove(m)
# print(b)
a = [1,0,-1,-2,1,-1,0]  
i = 0
x = len(a)-1
j = x
while True:
    if a[j]<a[i]:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    j-=1
    if j == i:
        j = x
        i+=1
    if i == x:
        break
    # print(a)

print(a)