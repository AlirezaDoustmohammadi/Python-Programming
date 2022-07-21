
list1 = ['a', 'b', 'c', 'd' , 'a']  # 'abcd'

#print('-'.join(list1))

# del, remove , pop


list1 = [element for element in list1 if element != 'a']

print(list1)
del [list1[0]]
list1.pop(0)

print(list1)
