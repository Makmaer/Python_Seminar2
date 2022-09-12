# 1. Подсчитать сумму цифр в вещественном числе.
x=-10.1234
n=x
if n==0:
    count=1
elif n<0:
    count=0
    x=-x  
else:
    count=0 
while n>0:
    count+=1
    n=n//10
s=str(x)
ZnakPosleZap=len(s)-(count+1) #Не смог придумать, как посчитать занки после запятой без перевода в строку. Возможно ли вообще?
count=count+ZnakPosleZap
print('всего цифр:', count)
sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print('сумма цифр:', sum)

