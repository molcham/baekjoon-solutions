'''
정수 n 은 11보다 작다
1
2 = 1 1 , 2
3 = 1 1 1 , 1 2 ,2 1, 3  4가지
5= 11111 1121*4 113*3 23 32
6= 11111 11121*5 1131*4 123*3 33 222
7= 111111 111112*6 11113*5 123  존니 많다...

123을 쓰는 순열? 순서 상관 없으니께 이 순열의 합이 n 이여야함 

중복 허용

4 
5 
6
7
8
9
10
11

for i in range (n):
    new_list=list(combinations(my_list,i+1))
    for j in range (len(new_list)):
        hap=sum(new_list[j])
        if s==hap:
            answer=answer+1

print(answer)

아닌가봄..답안나오뮤뮤

'''
from itertools import *

n=int(input())
answer=0

my_list=[1,2,3]

for i in range(n):
    c=n
    new_list=list(permutations(my_list,i+1))
    for j in range (len(new_list)):
        hap=sum(new_list[j])
    if c==hap:
        answer=answer+1
print(answer)



