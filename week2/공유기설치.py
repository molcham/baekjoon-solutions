'''

1. 공유기 사이 거리를 x로 설정 (mid)
2. x를 기준으로 공유기 설치 
3. 공유기를 c개이상 설치할 수 있다. 
   =>여유가 있다. x보다 짧은 거리는 볼 필요없이 거리를 늘려서 최댓값을 확인
4.재귀를 통해 찾은 최댓값 반환?

우현님 설명 

거리를 a라고 정해두고고





'''
#반복문으로 작성하기
#mid를 반씩 줄여나가는?
#mid는 공유기 거리


import sys

def wifi_search(arr,target,n):
    left,right=0,n #탐색 범위 설정
    while left<=right:
        mid=(left+right) // 2
        if (len(arr)//mid)+1==target:
            return mid
        elif (len(arr)//mid)+1 <target:
            right=mid-1
        else:
            left=right+1
    return mid

n,c=map(int,input().split())

#home_list=sorted(map(int,(sys.stdin.read().split())))
home_list = sorted(int(input()) for _ in range(n))  # N번 입력받아 정렬

print(wifi_search(home_list,c,n))











