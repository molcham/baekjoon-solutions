'''
최대 힙 = 우선순위 큐 

출력은 입력에서 0이 주어진 횟수만큼 한다.
x가 0 이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거

아 우선순위 큐는 기본적으로 작은 수 부터 출력!
최대 힙은 음수로 바꿔서 저장해줘야함 !
'''
import sys
import heapq

pq=[]
n=int(sys.stdin.readline())


for i in range(n):
    command=int(sys.stdin.readline()) #입력 받기
    if command>0:
        heapq.heappush(pq,(-command))
    else:
        if len(pq)==0:
            print(0)
        else:
            print(-heapq.heappop(pq))
            
        
    
    



    






