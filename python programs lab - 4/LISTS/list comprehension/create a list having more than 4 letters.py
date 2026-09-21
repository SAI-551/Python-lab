# Given a list of words, use a list comprehension to create a new list containing only the words with more
#than 4 letters

list=["mani","ram","manohar","yashwanth"]
list1=[list for list in list if len(list)>4]
print("new list having more than 4 letters in list:",list1)


#output:

#new list having more than 4 letters in list: ['manohar', 'yashwanth']
