#B7. Identity Operators
#Operators: is , is not
#Task B7.1: Create two lists with the same content, list1 and list2, and a third variable list3 = list1. Use
#the is and is not operators (along with id()) to check and explain which variables refer to the same
#object in memory.
list1 = [3, 4, 5]
list2 = [3, 4, 5]
list3 = list1
print(list1 == list2) #True
print(list1 is list2) #False 
print(list1 is list3) #True
print(id(list1), id(list2), id(list3))#2948951830400 2948951821376 2948951830400


