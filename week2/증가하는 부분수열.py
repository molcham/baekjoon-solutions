'''
가장 긴 증가하는 부분수열 
이분탐색 사용하기

등차수열일 필요 없음
그냥 증가하기만 하면됨
a={10,20,10,30,20,50} 일때 {10,20,30,50}
정렬하면 {10,10,20,20,30,50}
mid =20

제일 작은

1.데이터 정렬하기 
2.앞에서 부터 하나씩 검사?
3.만약 크면 넣고, 이미 리스트에 존재하는거면 안넣고 넘어감
4.만약 마지막 원소까지 검사완료하면 탐색 끝
5.새로 생성된 리스트 반환하고 끝



'''
'''
n=int(input())
my_list=sorted(map(int,input().split())) #입력받은 리스트 정렬하기 
answer_list=[my_list[0]]

minn=my_list[0] #정렬했을 때 제일 작은 원소 넣어주기

for i in my_list: #my_list에 있는 원소 검사
    if i not in answer_list and i>minn: # min/max 는 변수명으로 사용하면 안됨됨
        answer_list.append(i)
        minn=i

print(len(answer_list))

이 코드로 구현할 경우 최악의 경우 O(n**2)의 시간복잡도
=> 더 효율적인 코드가 필요함

'''
'''def binary_search_left(arr, target):
    """이진 탐색으로 target이 들어갈 왼쪽 위치 찾기"""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1 #탐색부분을 반으로 줄이는 부분!
        else:
            right = mid

    return left  # target이 들어갈 위치 반환

n = int(input())
my_list = sorted(map(int, input().split()))  # ✅ 정렬 필수
answer_list = []  # 중복 제거된 리스트

for num in my_list:
    idx = binary_search_left(answer_list, num) 
     # ✅ 이진 탐색으로 중복 검사

    # ✅ 중복이 없을 경우에만 추가
    if idx == len(answer_list) or answer_list[idx] != num:
        answer_list.insert(idx, num)  # ✅ 정렬된 상태 유지하며 삽입

print(len(answer_list))  # ✅ 고유한 원소 개수 출력


'''
#bisect.bisect_left()
#증가하는 수열 문제에서 정렬을 하면 그냥 최장 정렬된 수열이 나온다.
#정렬을 안하고 찾아야 '최장 증가 수열'을 찾을 수 있음 
#bisect이용해서 나무 자르기 문제 풀어보기
import bisect

n=int(input())

my_list=sorted(map(int,input().split()))
lis=[] #마지막으로 반환할 증가하는 부분수열

for num in my_list:
    idx=bisect.bisect_left(lis,num)
    if idx ==len(lis):
        lis.append(num) #lis의 마지막 값보다 크면 추가 
    else:
        lis[idx] =num #만약 겹치는 수 나오면 똑같은 수지만 교체 

print(len(lis))





        
    









