# 5. Реализуйте алгоритм перемешивания списка.
from random import randint


n=6
list1=[]
list2=[]
for i in range(n):
    list1.append(randint(0,10))
print(list1)
for i in range(n):
    el1=list1.pop(randint(0,len(list1)-1))
    list2.append(el1)
print(list2)