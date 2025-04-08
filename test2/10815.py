'''
숫자 카드 n개 -1번째 줄
숫자 카드에 적혀있는 정수 -2번째 줄
정수 m ,상근이가 가지고 있는지 구분해야 할 카드갯수 -3번째 줄
구분 해야할 숫자카드에 적혀있는 정수 -4번째 줄

터미널 실행하면 잘되는데...백준은 시간초과 ^.ㅠ 아임파인...
아마 탐색법 써야하나보다..분할탐색??..

탐색법은 이진탐색쓰기 bisect



set사용하기 ! ! 시간초과 안남남

'''


import sys

input=sys.stdin.readline

n=int(input())
geun_list=list(map(int,input().split()))

m=int(input())
check_list=list(map(int,input().split()))

result=[]

for i in range (m):
    if check_list[i] in geun_list:
        result.append(1)
    else:
        result.append(0)
print(*result)

'''

import sys
input=sys.stdin.readline

n=int(input())
geun_list=sorted(list(map(int,input().split())))
#작은 것 부터 정렬하기

m=int(input())
check_list=sorted(list(map(int,input().split())))
#작은 것 부터 정렬하기 

result=[]

#분할 탐색 ㅜㅜ구현..?

def check_geun(arr1,arr2):
    for i in range len(arr1):
      target=arr[i]
      left,right=0,len(arr1)-1
    


'''





