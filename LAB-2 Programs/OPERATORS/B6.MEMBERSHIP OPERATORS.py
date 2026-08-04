#B6. Membership Operators
#Operators: in , not in
#Task B6.1: Create a list of five fruits. Ask the user to enter a fruit name and check whether it is in the list
#or not, using the in and not in operators.
fruits = ["apple", "banana", "mango", "grape", "kiwi"]
item = input("Enter a fruit: ")#enter a fruit:banana
print(item, "is in the list:", item in fruits)#banana is in the list:True
print(item, "is not in the list:", item not in fruits)#banana is in the list:False
