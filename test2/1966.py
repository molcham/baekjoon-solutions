'''

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
그렇지 않다면 바로 인쇄를 한다.

프린터 큐
큐 사용하기 
숫자 비교 후 크면 남기고 작으면 popleft해서 바로 뒤로 append하기 
3 
1 0 문서개수 1개,0번째로 놓여있음 
5 중요도 5 
=> 저 중요도 5번이 몇번째로 출력? => 첫번째

4 2 문서개수 4개, 0,1,'2'번째로 놓여져있음
1 2 3 4 중요도 각 1 2 3 4  저 중요도 3번이 몇번째로 출력?
=>4123 312 21 1

6 0 문서개수 6개 , 0번째로 놓여져 있음
1 1 9 1 1 1 중요도 각 다음과 같음
=> 저 '0'번째에 있는 1  몇번째로 출력?
=> 9앞에 있는 1 뒤로 보냄

문제점1.애초에 case에 몇개의 테스트 케이스 입력받을지 받고 
그 수만큼 연달아 입력 받는 기능을 구현을 못함

문제점2.deque에 잘못된 방식으로 저장했는지,,,자꾸 popleft가 안됨 흑

문제점3.아마 출력결과도 한 리스트에 모아두었다가 출력해야 할것같은데
구현못함 헷

'고'재웅 님의 풀이 깃허브에서 확인하기

나와의 공통점
q=deque()사용하심
max함수 사용하심


'''
from collections import deque
import sys


input=sys.stdin.readline

#case=int(input()) # 테스트 케이스의 개수

n,m=map(int,input().split()) #문서의 개수,알고 싶은 문서의 순서
score=map(int,input().split()) #n개 문서의 중요도
queue=deque() # 프린트 저장할 큐 

for k in score:
    queue.append(k)
    



#예를 들어 case2번의 문서를 알고 싶다.
count=0
target=queue[m]

if len(queue)<=1:
    print(1)
else:
    for i in range(n):
        out=max(queue)
        if queue[i]>=out:
            queue.popleft()
            count+=1
            if queue[i]==target:
                print(count)
                break
        else: #queue[i]<max
            x=queue.popleft()
            queue.append(x)

            
        

        











