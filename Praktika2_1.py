# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
N=5
list=[1]
for a in range(1,N):
    x=list[-1]
    list.append(x*(-3))
print(list)
