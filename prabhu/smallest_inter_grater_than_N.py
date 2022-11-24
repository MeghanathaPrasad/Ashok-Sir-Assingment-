# n = input()
# n1=int(n)
# l = len(n)
# s = set(n)
# ls=len(s)
# n2=[]
# if l == ls:
#     ns=int(n)
#     ns+=1
#     print(ns)
# for i in (n):
#     n2.append(int(i))
# k=0
# p=1
# if l !=ls:
#     for i in range (len(n2)-1):
#         t = n2[:k]
#         if n2[i] not in t:
#             if n2[k]==n2[p]:
#                 n2[p]=n2[p]+1
#                 print(n2)
#             else:
#                 mm = n2[:k]
#         else:
#             n2[i]=0
#             print(n2)
#         p+=1
#         k+=1
# print(t)
# print(n2)
       


# print(l)
# print(s)
# print(ls)

# n = 123456
# n1=[]
# m = str(n)
# # s=",".join(m)
# # print(type(s))
# for i in (m):
#     n1.append(int(i))
# for i in range(len(n1)-1,0-1):
#     print(n1[i],end=" ")


# l = [1,2,3,4,5]
# l[2]=l[2]+1
# print(l)



def solution(n: int) -> int :
    n += 1

    while True:            
        s = str(n) # 99 [4 4 4 3 2]
        flag = True
        # for i, v in enumerate(s[1:]):
        #     if s[i] == v:
        #         flag = False
        #         break
        #in range method
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                flag = False
                break

        if flag:
            return n
        n += 1
    return 0

print(solution(int(input())))