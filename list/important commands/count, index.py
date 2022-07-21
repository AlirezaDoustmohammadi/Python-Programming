

list1 = ['a', 'b', 'c', 'd' , 'a'] #--> [0 , 4]

list2 = ['m' , 'a' , 'n']


list3 = set(list1) - set(list2)

# list4 = set(list1)- set(list3)
list4 = set(list1).intersection(set(list2))

print(list(list4))

#print(list1.index('a'))

#print(list1.count('a'))

element_index = []
for index , element in enumerate(list1):
    if element == 'a':
        element_index.append(index)



#print(element_index)
