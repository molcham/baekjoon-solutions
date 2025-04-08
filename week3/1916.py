'''
최소 비용 구하기 : 다익스트라 알고리즘 

'''
import heapq
import sys

input=sys.stdin.readline

def find_dijkstra(graph,start,end):
    dist={node:float('inf') for node in graph}
    dist[start]=0 # 시작 노드의 거리는 0(나 자신과의 거리는 0이니까)
    queue=[(0,start)] #우선 순위 큐의 초기화

    while queue:
        current_dist,current_node=heapq.heappop(queue)

        if current_dist>dist[current_node]:
            continue
        for neighbor,weight in graph[current_node]:
            distance=current_dist +weight
            if distance < dist[neighbor]:
                dist[neighbor]=distance
                heapq.heappush(queue,(distance,neighbor))
    return dist[end] # 목적지 노드까지의 최소 비용 end가 목적지니까 

n=int(input()) #도시의 개수
m=int(input()) #버스의 개수
bus_list={i: [] for i in range(1, n+1)}
#미리 딕셔너리 초기화 해주기

for i in range (m):
    a,b,cost=map(int,input().split())
    bus_list[a].append((b,cost))
'''
입력받은 그래프:
1 → [(2, 2), (3, 3), (4, 1), (5, 10)]
2 → [(4, 2)]
3 → [(4, 1), (5, 1)] 3에서4가는거 비용 1
4 → [(5, 3)] 4에서5가는거 비용 3
5 → []
'''

start,end=map(int,input().split())
#출발지,도착지 받기

print(find_dijkstra(bus_list,start,end))

