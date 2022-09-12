# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число. (например:positions = [1, 3, 6]).
n=4
pr=1
list0=''
list1=[]
for i in range(-n,n+1):
    list1.append(i)
with open ('list2.txt', 'r') as file:
    list0=file.readline()
list2=list0.split(',')
print(list1)
print(list2)
for i in list2:
    pr=pr*list1[int(i.strip())]
print(pr)
