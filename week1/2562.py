my_list=[0]*9
for i in range(9):
    k=int(input(""))
    my_list[i]=k

a=my_list[0]
for z in range(8):
    a=my_list[0]
    if my_list[z]>a:
        a=my_list[z]

print(a)
print((my_list.index(a))+1)

'''

numbers = []
for j in range(9):
    i = int(input())
    numbers.append(i)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)


'''