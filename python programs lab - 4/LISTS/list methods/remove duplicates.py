#Write a program to remove duplicate elements from a list without using the set() function.
list=[10,20,30,40,10,20]
list1=[]
for value in list:
    if value not in list1:
        list1.append(value)

print("original list:",list)
print("after removing duplicates:",list1)
#output:
#original list: [10, 20, 30, 40, 10, 20]
#after removing duplicates: [10, 20, 30, 40]

