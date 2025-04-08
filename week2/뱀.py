'''
큐를 이용하는 문제

1.사과가 있을 때 : 머리(움직임) 중간(늘어남) 꼬리(그대로) 
2.사과가 없을 때 : 머리(움직임) 중간(그대로) 꼬리(움직임)

큐를 사용하여 뱀의 몸통을 관리하면서
=> "머리를 이동시키고, 꼬리를 유지/제거 하는 방식"

1.큐를 사용해야 하는 이유
뱀의 몸은 선입선출 방식으로 변함(큐)
앞에서 새로운 위치를 '추가'하고 '꼬리는 제거' 해야함
이러한 동작이 큐의 동작과 동일 => deque이용하기

popleft() => 큐의 맨 앞의 원소를 제거하는 연산
deque에서는 가장 먼저 들어온 요소를 제거 

항상 마지막에 추가된애가 머리의 좌표임!
snake = deque([(1,1), (1,2), (1,3)])  # ✅ 초기 뱀 위치 (머리: (1,3))

# 새로운 머리 추가 (오른쪽으로 이동)
snake.append((1,4))
print(snake)  # 출력: deque([(1,1), (1,2), (1,3), (1,4)])

머리는 항상 이동하니까 마지막에 이동해서 들어온 (1,4) 가 머리다!

(1,1) 꼬리는 쌓아놨다가 만약에 사과가 없어서 이동하면 popleft()로 제거! 

!!좌표 기준이 아니라 행렬 기준으로 생각해야됨!!
즉 오른쪽 왼쪽 꺾어도 행렬만 증가하기 때문에 음수가 될일은 없음!

'''

from collections import deque
import sys

input = sys.stdin.readline
n=int(input()) #보드의 크기
k=int(input()) #사과의 개수
apples=[]

for _ in range(k):
    r,c = map(int,input().split()) # 사과의 행,열 입력 받기
    apples.append((r,c)) #튜플 형태로 리스트에 저장

l=int(input()) #뱀의 방향 변환 횟수

turns={}

for _ in range(l):
    times,directions=input().split() 
    #turns.append((int(times),directions)) #(숫자,문자) 튜플로 리스트에 저장
    turns[int(times)]=directions

snake=deque([(0,0)]) #뱀의 초기위치 및 지금 뱀의 위치를 넣어줄 큐
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # ✅ 우 → 하 → 좌 → 상
idx=0 #초기 방향 (오른쪽)
x,y=0,0 # 뱀의 초기 머리 위치
time=0

'''
다 받은 다음 해야하는 일

공통적으로 처리해야 하는 것
벽에 닿거나, 자기 자신에 닿지 않으면 계속해서 움직이기
만약 닿으면 바로 종료하면서 몇초에 끝났는지 출력


1)turns안에 있는 times 까지
1-1.사과가 있는 칸까지는 머리 중간 꼬리 넣고 꼬리는 삭제 머리는 추가 해주기
1-2.if 사과가 있는 칸이라면 머리만 새로추가 
2)times가 다됐다면 directions의 방향에 따라 (L,D) 방향 바꾸기
2-1.다음 시간이 될때까지 조건에 따라 1번루틴 다시 반복 

'''

while True:
    time+=1 #1초 증가

    x,y=snake[-1] #제일 최신의 위치
    dx,dy = directions[idx] #방향 정보,어디방향으로 나아갈 건지
    nx,ny=x+dx,y+dy #새로운 머리 위치 현재위치에서 dx,dy방향으로 나아간 위치

    if nx<0 or nx>=n or ny<0 or ny>=n or (nx,ny) in snake:
        print(time)
        break

    if (nx,ny) in apples:
        apples.remove((nx,ny))
        snake.append((nx,ny))
    else:
        snake.append((nx,ny))
        snake.popleft() #꼬리 제거,제일 앞에있는 요소 제거하기
    

    if time in turns:
        if turns[time]=='D': #오른쪽 회전해주기
            idx=(idx+1)%4 
        elif turns[time]=='L':
            idx=(idx-1)%4















