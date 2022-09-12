# 2 Написать программу получающую набор произведений чисел от 1 до N.
n=4
list=[1]
list[0]=1
for i in range(1,n):
   list.append(list[i-1]*(i+1)) 
print(list)
