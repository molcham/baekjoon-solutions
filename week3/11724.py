'''

방향 없는 연결 그래프 

몇개의 그룹으로 나눠져 있는지를 파악하는 문제

연결 요소 : 그래프에서 서로 이어져 있는 노드들의 묶음
연결 요소 개수: 그래프 전체에서 독립된 그룹이 몇 개인지


dfs로 각 그룹을 찾고 세기
=> 가능한 깊게 탐색하기, 어디까지 이어져있나 탐색 하기

1.모든 노드를 돌면서 
2.만약 그 노드를 방문하지 않았다면 , 거기서 부터 dfs를 탐색하기
3.그 dfs는 하나의 연결 요소 전체를 방문하게 된다.
4.그러면 연결 요소 카운트를 하나 늘려준다
5.이 과정을 모든 노드에 대해 반복 한다.


'''

import sys
input=sys.stdin.readline

n,m =map(int,input().split())
#첫째 줄에 정점의 개수 n과 간선의 개수 m이 주어진다.

#visited=set()

my_list=[]

'''
지금 graph는 간선 기준으로만 만들고 있기 때문에
연결되지 않은 노드는 아예 키조차 생기지 않는다

모든 정점이 기본적으로 빈 리스트라도 갖고 있어 에러가 방지됨
'''
graph={i: [] for i in range(1, n+1)}

for i in range (m):
    a,b =map(int,input().split())
    my_list.append((a,b)) #라스트 쌍 입력 받기

for a,b in my_list:
    graph.setdefault(a,[]).append(b)
    graph.setdefault(b,[]).append(a)  #graph 만들어짐

'''

visited: 방문한 노드를 저장하는 집합
path: 방문한 노드의 순서를 기록하는 리스트

'''
def dfs(node,visited,path):
    visited.add(node)
    path.append(node)
    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            dfs(neighbor,visited,path)
    return path
#연결 요소 개수 세기
visited_dfs=set()
count=0

for i in range(1,n+1):
    if i not in visited_dfs: #1부터 n까지의 정점중에 DFS에서 빠진애가 있으면
        path_dfs=[] # 방문 순서를 저장한다
        dfs(i,visited_dfs,path_dfs) #재귀 호출
        count += 1 # 새로운 연결 요소 발견

print(count)













