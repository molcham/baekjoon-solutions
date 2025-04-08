'''
-- 가 같은 행에 있다면 같은 나무 판자
ㅣㅣ 가 같은 열에 있다면 같은 나무 판자 

인접...행렬??에서 체크하기?
만약 -라면 j를 플러스 해주면서 확인
만약 | 라면 i를 플러스 해주면서 확인 

크게는 while로 짜고

안에서는 if로
2개로 나눠서 짜기 continue 넣어서 

모르겠다!!!!!!!!!!! ㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜ

만약 이어진다 큐에넣기 
만약 다른게 나온다  bfs로 count로 새주기
다른거 나올때 ...count해주기 -도연님 풀이 

'''

'''
이 코드의 문제점
1.home을 빈 리스트로 만들고 나서
2.home[i][j]에 직접 값을 대입하려고 하면
3.home[i]도 없고 , home[i][j]도 없기 때문에
  => indexError가 나면서 입력이 안된다. 
'''
'''
#세로크기 n , 가로 크기 m 
home=[]

#home 인접행렬 입력받기
for i in range (n):
    for j in range(m):
        home[i][j]=input()
        # 일단 여기서 입력부터 안받아짐




# 이것 뭐에요 뭐 이리 많이 변수를...
count=0

block1=0
block2=0

row=0
col=0
now=home[row][col]


#마지막 블록까지
while count<n*m:
 #하나씩 보다가 만약 '|'가 나오면 탐색방향을
 #바꿔줘야 하는데 모르겠음 이걸!!!!!!!!!!!!!
    if now=='-':
        now=home[row][col+1]
        count+=1

'''
import sys
input=sys.stdin.readline 

n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
#2차원 방문 배열 초기화 코드
#n행 m열짜리 2차원 배열에서 각 칸 방문여부 체크
visited=[[False]*m for _ in range(n)]
#일단 방문 안했으니까 false로 초기화














 





