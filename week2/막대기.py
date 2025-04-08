'''
스택을 이용한 문제

맨 끝쪽에 있는=맨 마지막에 들어간 top(),pop()

그 원소보다 크면 보임 ! 큰 것 찾기




'''



'''
for i in range(n):
    block=int(input())
    if i==0:
       my_list.append(block)
    elif my_list and block>=my_list[-1]: #리스트의 바로 이전 원소
        my_list.pop()
        my_list.append(block)
    else:
        my_list.append(block)
for j in my_list[:-1]:
    if j> my_list[-1]:
        count +=1

print(count+1)
for j in range(n-1,-1,-1)
'''
import sys # 그냥 input()으로 하면 시간초과 난다 !
my_list=[]
count=1 # 맨앞에 있는 막대기는 무조건 보임 
n=int(sys.stdin.readline())

for i in range(n): 
    block=int(sys.stdin.readline())
    my_list.append(block)


#가장 큰 막대기를 기준으로 check해야됨
max_block=my_list[n-1]

for j in reversed(my_list):
    if j>max_block:
        max_block=j
        count+=1
print(count)





    






    













