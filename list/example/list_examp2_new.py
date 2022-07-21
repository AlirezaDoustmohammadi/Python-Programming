
from operator import itemgetter

list1 = [['a',10],['b',1]]

#list1 = ['bcdm','aaaaaaaa']


print(sorted(list1 , key = itemgetter(1)))
