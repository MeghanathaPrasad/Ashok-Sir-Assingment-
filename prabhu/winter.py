l = [-3,-14,-5,7,8,42,8,3]
#l=[2,-3,3,1,10,8,2,5,13,-5,3,-18]
#l=[1,-6,500,-4,12,3,1,-7,3,7,100,200]
#print(l)
v = len(l)//4
#print(v)
t = 0 
l2=[]
m=[]
r=[]
for i in l:
    r.append(abs(i))
#print(r)
for i in range(1,len(r)+1,v):
    l3=r[t:i+2]
    l2.append(l3)
    t+=v
#print(l2)
for i in range(len(l2)):
    m.append(abs((min(l2[i])-max(l2[i]))))
#print(m)
mx = max(m)
mx1 = m.index(max(m))
match mx1:
    case 0 : print(f"moduls is WINTER")
    case 1 : print("SPRING")
    case 2 : print("SUMMER")
    case 3 : print("AUTUMN")

'''another way
def solution(arr):
    seasons=["winter","spring","summer","autumn"]
    temp=[]
    n = len(arr)//4
    for i in range(0,len(arr),n):
        mx =max(arr[i:i+n])
        mn =min(arr[i:i+n])
        temp.append(abs(mn-mx))
    return seasons[temp.index(max(temp))]

arr = [-3,-14,-5,7,8,42,8,3]
arr = [2,-3,3,1,10,8,2,5,13,-5,3,-18]
print(solution(arr))'''




    