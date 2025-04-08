'''
위상 정렬 문제

역추적 할때는 dfs를 사용해서 몇개인지 찾고, 
경로를 출력할 수도 있다 

출발도시 : 진입차수가 0
도착도시 : 진출차수가 0

위상정렬 + 가중치 포함 으로 푸는 복합적인 그래프 문제

a,b,c 한줄에 입력받기  m+2까지
a : 도로의 출발 도시의 번호
b : 도로의 도착 도시의 번호
c : 이 도로를 지나는데 걸리는 시간

m+3 : 출발도시와 도착도시 한줄에 입력 받기  

출력 1st: 모든 사람이 만나는 시간
출력 2nd: 모든 사람이 만나는 시간까지 계속 달려하는 도로
=> 최장 경로에 포함된 간선의 수


'''
import sys
from collections import deque

input=sys.stdin.readline

n=int(input()) #도시의 개수
m=int(input()) #도로의 개수

adj=[ [] for _ in range(n+1) ] #인접 리스트
indegree=[0]*(n+1) #진입 차수
time = [[0] * (n + 1) for _ in range(n + 1)] 

for _ in range(m):
    a,b,t = map(int,input().split()) #a->b a가 먼저
    #a도시,b도시,걸리는 시간 t
    adj[a].append((b,t)) #인접리스트로 저장해주
    indegree[b] += 1 
    #b의 진입차수 1 증가 시켜주기

#위상 정렬 시작
queue = deque()
for i in range(1,n+1):
    if 






