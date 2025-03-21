'''
완전 탐색 

순열 :주어진 요소들을 순서를 고려하여 나열하는 모든 경우의 수를 의미한다.
내가 생각한 풀이는 중간값과 비교하기?....


No!!완전탐색으로 모든 경우의 수를 구해서 
모든 순열을 구하기 위해서 순열 라이브러리를 사용하기 
'''

from itertools import permutations
n=int(input())

#my_list의 크기는 n이다

my_list=map(int,input().split())

p=list(permutations(my_list,n))  # 순열 만들어 주기, n은 리스트에 저장된 값의 수
# 값의 수를 생각해서 순열로 랜덤 만들으로 만들어주기기

answer=0

for i in p: # i가 튜플 p안에 있을 때
    s=0  # 합은 0으로 초기화

    #반복문으로 튜플을 꺼내 각 순열마다 차이의 합(s) 를 구하고 , 최댓값을 answer에 저장하기
    for j in range(n-1): #만약 n=4라면 0,1,2 이렇게 3번 연산
        s+=abs(i[j]-i[j+1]) # 각 순열마다 차이의 합을 구하기

    answer=max(answer,s)

    #모든 경우의 원소들 끼리의 차이의 절댓값의 합을 a-max함수를 이용하여 갱신

print(answer)
    











