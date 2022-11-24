
from time import time
def for_loop(n= 100000000):
    start_time = time()
    s = []
    for i in range (n):
        s.append(i)
    end_time = time()

    return "time taken to execute while loop:" ,end_time-start_time

print(for_loop())

def while_loop(n=100000000):
    start_time = time()
    i = 0
    s = []
    while i<n:
        s.append(i)
        i +=1
    end_time = time()
    return "time taken to execute for loop:" ,end_time-start_time

print(while_loop())


# def sum_range(n=100):
#     return sum(range(n))

# sum_range()


# def sum_numpy(n=1000):
#     # start_time = time()
#     return numpy.sum(numpy.arange(n))

# sum_numpy()
    

# def for_loop(n= 100000000):
#     start_time = time()
#     s = []
#     for i in range (n):
#         s.append(i)
#     end_time = time()

#     return  end_time-start_time


from time import time


# l = []
# def printList(n):
#     start_time = time()
#     if (n>0):
#         l.append(n)
#         printList(n-1)
#     end_time = time()    
#     return start_time-end_time


# if __name__ == "__main__":
#     start_time = time()
#     n = int(input("enter n: "))
#     printList(n)
#     l.reverse()
#     print("1 to n numbers : ",l)
#     end_time = time()   



