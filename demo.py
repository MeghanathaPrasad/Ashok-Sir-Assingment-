

# s="meghu prasad"
# c = 0
# b=[]
# for i in range(len(s)):
#     if s[i] == " ":
#         c+=1
#         if c == 1:    
#             k = s[i:0:-1]
#         # elif c==2:
#         #     j = s[]                         
#         # for j in range(p):
#         #     b.append(s[j])
#         # #elif count ==2:
# print(c)
# print(k)
# k = s[5::-1]
# print(k)
#hacker rang 
# l = [2,5,1,8,9,3,7]
# l_indx=[]
# l1=[]
# l2=[]
# l3=[]
# for i in range(len(l)):
#     l_indx.append(i)
# for i in range(len(l_indx)):
#     if l_indx[i]%2==0:
#         l1.append(l[i])
#     else:
#         l2.append(l[i])
# l1.sort(reverse=True)
# l2.sort()
# k=1
# for i in range(len(l2)):
#    l1.insert(k,l2[i])
#    k+=2
    
# print(l)
# print(l1)


# n=[4,4,4,5,3]
# k=1
# for i in (n):
#     for j in range(len(n)):
#         if i == n[k]:
#             n[k]=0
#         else:
#             n[j]=n[j]
#         k+=1
            
# print(n)
n= 3298
le = len(str(n))
sn = set(str(n))

def sett(n):
    return len(set(str(n)))

# print(sn)
# ss=""
# for i in sn:
#     ss+=i
# sss = int(ss)
# # while n>0:
# #     if len(sn)==

for i in range(n,n*2):
    s=sett(i)
    if s == le:
        ii = i
        break

print(ii)