#Write a program that merges two lists and sorts the combined list in descending order
list1=[3,2,1,5,6]
list2=[12,7,9,15,13]
combined_list=list1+list2
print("combined list:",combined_list)
order=sorted(combined_list)
descending_order=order[::-1]
print("descending order:",descending_order)


#output:
#combined list: [3, 2, 1, 5, 6, 12, 7, 9, 15, 13]
#descending order: [15, 13, 12, 9, 7, 6, 5, 3, 2, 1]



