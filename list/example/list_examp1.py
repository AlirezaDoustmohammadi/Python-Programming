
list1 = [2,4,6,8,['m',2],0 , -1 , ['b',10]]

list1_single_value_type = []
list1_list_value_type = []

#element base for element in list
# for index in range()
# for index , element in enumrate(list)

for element in list1:
    if type(element) == list:
        list1_list_value_type.append(element)
    else:
        list1_single_value_type.append(element)


list1_list_value_type = sorted(list1_list_value_type)
print(list1_list_value_type)
list1_single_value_type = sorted(list1_single_value_type)
list1 = []
list1.extend(list1_single_value_type)
list1.extend(list1_list_value_type)
print(list1)
    
