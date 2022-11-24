
   # Python program to copy or clone a list Using the Slice Operator
# def Cloning(L1):
#     L2_copy = L1[:]
#     return L2_copy
 

# L1 = [4, 8, 2, 10, 15, 18]
# L2 = Cloning(L1)
# print("Original List:", L1)
# print("After Cloning:", L2)


# # Python code to clone or copy a list Using the in-built function extend()
# def Cloning(L1):
#     L2_copy = []
#     L2_copy.extend(L1)
#     return L2_copy
   
# # Driver Code
# L1 = [4, 8, 2, 10, 15, 18]
# L2 = Cloning(L1)
# print("Original List:", L1)
# print("After Cloning:", L2)



# # Python code to clone or copy a list Using the List copy using = 
# def Cloning(L1):
#     L2_copy = L1
#     return L2_copy
   
# # Driver Code
# L1 = [4, 8, 2, 10, 15, 18]
# L2 = Cloning(L1)
# print("Original List:", L1)
# print("After Cloning:", L2)

# # importing copy module
# import copy
   
# # initializing list 1
# L1 = [1, 2, [3,5], 4]
   
# # using copy for shallow copy 
# L2 = copy.copy(L1)
 
# print(L2)

# # Python code to clone or copy a list Using list comprehension
# def Cloning(L1):
#     L2_copy = [i for i in L1]
#     return L2_copy
   
# # Driver Code
# L1 = [2, 4, 6, 8, 10, 12]
# L2 = Cloning(L1)
# print("Original List:", L1)
# print("After Cloning:", L2)

# # Python code to clone or copy a list Using append()
# def Cloning(L1):
#     L2_copy =[]
#     for item in L1: L2_copy.append(item)
#     return L2_copy
   
# # Driver Code
# L1 = [4, 8, 2, 10, 15, 18]
# L2 = Cloning(L1)
# print("Original List:", L1)
# print("After Cloning:", L2)

# Python code to clone or copy a list Using bilt-in method copy()
def Cloning(L1):
    L2_copy =[]
    L2_copy = L1.copy()
    return L2_copy
   
# Driver Code
L1 = [10, 20, 30, 40, 50, 60]
L2 = Cloning(L1)
print("Original List:", L1)
print("After Cloning:", L2)


# # importing copy module
# import copy
   
# # initializing list 1
# L1 = [1, 2, [3,5], 4]
 
# # using deepcopy for deepcopy 
# L2 = copy.deepcopy(L1)
# print(L2)