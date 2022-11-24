# list.append(value) # Append a value.
# list.extend(iterable) # Append a series of values.
# list.insert(index, value) # At index, insert value.
# list.remove(value) # Remove first instance of value.
# list.clear() # Remove all elements.

#updating list with append funtiong--->in this append function the value will be added at the end of the list
l=[1,2,3,4,5,6,7,8,9,10]
l.append(11)
print(l)

#updating list with another list with extend funtion-->in this extend funtion the one list is added and the end of the another list 
l2=[10,20,30,40,50]
l3=[60,70,80]
l2.extend(l3)
print(l2)

#updating list with insert funtion--->in this insert funtion the value will be added at the required index position 
l4=[100,200,400,500,600]
l4.insert(2,300)
print(l4)

#updating list with remove funtion-->in this remove function the unwanted value in the list is remove by provied that value

l5=[5,10,15,20,21,25,30]
l5.remove(21)
print(l5)

#updating list with clear funtion--->in this clear function the the list will be becoming empty
l6=[2,4,6,8,10,12,14,16]
l6.clear()
print(l6)