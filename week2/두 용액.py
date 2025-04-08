'''
이분 탐색 문제

같은 양의 두 용액을 혼합한 용액의 특성 값 
=>혼합에 사용된 각 용액의 특성값의 합

같은 양의 두 용액을 혼합하여 특성값이 0에 가까운 용액을 만드려고 함

산성 용액 : 양수
알칼리성 용액: 음수

두 종류의 알칼리성 용액만으로나 두 종류의 산성 용액 만으로
특성값이 0에 가까운 혼합 용액 만들기 가능

두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가까운 용액을 
만들어내는 두 용액을 찾는 프로그램을 작성하시오

출력: 두 용액은 특성값의 오름차순으로 출력
특성값이 0에 가까운 용액을 만들어내는 경우가 두개 이상일 때 
=> 그 중 아무것이나 하나를 출력 

<내 풀이>
1.두개의 합이 가장 0과 가까운 것을 고르면됨
2.key point : 합이 0이 되려면 어떤 조합이 필요한지
3.-i 와 i 의 조합이 필요함

4.이분탐색 문제는 target을 어떻게 설정할지가 문제 !
5.bisect 사용하기

1.정렬하기 -99,-2,-1,4,98
2.bisect를 사용해서 target=-arr[i] 가 들어갈 위치 찾기
3.bisect_left(arr,target,i+1) 은 
target이 들어갈 수 있는 가장 왼쪽 위치를 반환
4.target 값이 그 인덱스값과 일치하지않고 그 값이 타겟보다 클 수 도 있음
5.하나 작은 인덱스도 확인을 해줘야 한다. 더 알맞은 값일 수도 있으니까!

idx = bisect.bisect_left(arr, target)  # 25가 들어갈 왼쪽 위치 찾기


'''

import bisect
import sys

n=int(sys.stdin.readline())
liquid_list=list(map(int,sys.stdin.readline().split()))

def find_liquid(arr):
    arr.sort()
    closet_sum=float('inf')  # 최소합을 무한대로 초기화 
    #만약 초기값을 0으로 하면 어떤값도 작을 수가 없다!
    reult=(0,0)

    for i in range(len(arr)):
        target =-arr[i]  #합이 0인게 제일 최적의 용액 서로 부호만 반대
        #들어갈 수 있는 가장 왼쪽 인덱스 반환
        idx=bisect.bisect_left(arr,target,i+1) # i를 기준으로 그 이후부터!
        #이진 탐색으로 위치 찾기

        for j in [idx-1,idx]: #현재 위치와 왼쪽 값 비교 (더 작을수도)
            if i<j<len(arr):
                mix=arr[i]+arr[j] #j 안에서 찾은 용액값
                if abs(mix)<abs(closet_sum): #절댓값으로 비교
                    closet_sum=mix
                    result=(arr[i],arr[j])
    return sorted(result)

print(*find_liquid(liquid_list))





