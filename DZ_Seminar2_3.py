# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = 6
list = {}
s = 0
for i in range(1, n+1):
    x = (1+(1/(i)))**(i)
    list[i] = x
    s += x
print(list)
print(s)
