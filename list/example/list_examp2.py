
list1 = [['a',10],['b',1]]

list_element_list = []

list_element_list_indx = []

for index , element in enumerate(list1):

    list_element_list.append(element[1])
    list_element_list_indx.append(index)



print(list_element_list)
print(list_element_list_indx)


sorted_index = [index for sorted_val,index in sorted(zip(list_element_list,list_element_list_indx))]

#print(sorted_index)

final_list = []

for indx in sorted_index:
    final_list.append(list1[indx])

print(final_list)
    
