#example
list1 = ["age",5]
tuple = ("sandy",list1)
#Now the tuple will contain,
("sandy",["age",5])
#we cannot modify the elements in a tuple but we are allowed to modify the list which will reflect in the tuple.
list1.append(10)
#Now the tuple will contain,
#("sandy",["age", 5, 10])
print(tuple)