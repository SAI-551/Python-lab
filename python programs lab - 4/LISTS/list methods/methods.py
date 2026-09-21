#Create a list of numbers and demonstrate the use of append(), insert(), extend(), remove(), pop(),
#sort(), reverse(), count(), and index() methods, printing the list after each operation

list=[1,2,3]
list.append(4)
print("append:",list)
list.insert(4,5)
print("insert:",list)
list.extend("m")
print("extend:",list)
list.remove("m")
print("remove:",list)
list.pop(4)
print("pop:",list)
list.sort()
print("sorted:",list)
list.reverse()
print("reverse:",list)

print("count:",list.count(4))
print("index:",list.index(4))
#output:
#append: [1, 2, 3, 4]
#insert: [1, 2, 3, 4, 5]
#extend: [1, 2, 3, 4, 5, 'm']
#remove: [1, 2, 3, 4, 5]
#pop: [1, 2, 3, 4]
#sorted: [1, 2, 3, 4]
#reverse: [4, 3, 2, 1]
#count: 1
#index: 0

