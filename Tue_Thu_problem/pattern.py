# n = int(input("enter number: "))
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     for j in range(n):
#         if i>=j:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
    
#     print()



n = int(input("enter number: "))
t = n*2//2
c = t
for i in range(n*2+1):
    if i <= (t):
        for j in range(t+1):
            if j <= t+1 and j >= t+1-i:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    
    else:
        for j in range(n*2+1):
            if j > t and j <= t+c:
                print("*",end="")
            else:
                print(" ",end="")
        c -= 1
        print()
    