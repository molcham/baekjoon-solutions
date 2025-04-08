'''

가장 효율적으로 카드를 합치는 방법

n개의 카드 묶음 각각의 크기가 주어질 때 
"최소한" 몇번의 비교가 필요한지 

우선 순위 큐?...


'''

import sys
import heapq
input=sys.stdin.readline

pq=[]
cards=[]

n=int(input())

for i in range (n):
    cards=list(input().split()) #입력 받기
print(*cards)



