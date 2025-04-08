'''
첫번째 줄 : 컴퓨터의 수
둘째 줄 : 네트워크 상에 직접 연결되어 있는 컴퓨터의 번호 쌍

3번째 줄 ~ n번째 줄 
한 쌍씩 네트워크 상에서 직접 연결되어 있는 번호 쌍

1=>2,5=>3,6

4개 : 2 5 3 6

<나의 생각>

n개의 쌍을 리스트에 저장하기
(인접 리스트에 넣기)

sick_list = [(1, 2), (2, 3), (4, 5)]

1번 컴퓨터 있는지 확인하기 
1번 컴퓨터와 인접해 있는 컴퓨터쌍 확인
인접해 있는 컴퓨터쌍과 인접해 있는 컴퓨터쌍 있는지 확인 

for 문으로 절대 못함 ...

위의 과정은 사실상 그래프 탐색 문제이다.


'''

import sys
#from collections import deque

visited=set()
#queue=deque([1])
input=sys.stdin.readline



com=int(input()) # 컴퓨터의 수
coms=int(input()) #연결된 컴퓨터 쌍의 수(간선의 수)

sick_list=[]
graph={}

for i in range (coms):
    a,b =map(int,input().split())
    sick_list.append((a,b)) #라스트 쌍 입력 받기

for a,b in sick_list:
    graph.setdefault(a,[]).append(b)
    graph.setdefault(b,[]).append(a)

#기본적인 dfs써주기!

def dfs(node,visited):
    visited.add(node)
    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            dfs(neighbor,visited)
visited=set()
dfs(1,visited)

print(len(visited)-1) #1번을 제외한 감염된 컴퓨터 수









    

