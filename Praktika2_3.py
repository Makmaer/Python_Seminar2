# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа 
# -определять количество вхождений одной строки в другой.
list1='в которой пользователь будет задавать две стороки ор'
list2='ор'

count = 0
for i in range(len(list1)):
    # print(list1[i:i+len(list2)])
    if list1[i:i+len(list2)] == list2:
        count +=1
print(count)


# count=0
# # print(list1.find('5'))
# while list1.find(list2) != -1:
#     x=list1.find(list2)
#     list1=list1[x+1:]
#     count+=1
# # count=0
# # for i in list1:
# #     if i== 'ор':
# #         count+=1
# print(count)