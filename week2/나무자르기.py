'''


존재하는 나무 리스트 중에서 제일 긴 나무가 뭔지 생각하기

1. sorted()로 정렬해주기 => list[n-1] , list[0] 
2.
넘치면 left : mid +1
부족하면 right : mid -1
3.
첫번째 이분탐색 : 주어진 나무들의 길이들의 리스트에서 한번 진행 
if: 첫번째 이분탐색에서 만약 맞는 길이 찾으면 종료
else: 두번째 이분탐색 시작 

4.첫번째 이분탐색에서

if 나무 부족으로 끝났는데 left=right 일 때  
=> 나무들이 다 존니 긴거임 0~arr[mid] 로 리스트 만들고 2차 이분탐색 

if 나무 넘침으로 끝났는데 left=right 일 때 
=> arr[mid]~arr[mid+1] 로 리스트 만들고 2차 이분탐색 




def geun_search(arr,target):
    left,right=0,len(arr)-1 #초기 인덱스 설정

    while left<=right:
        mid=(left+right) // 2
        total=sum((x - arr[mid]) for x in arr if (x-arr[mid]) >= 0 )

        if  total==target :
            return arr[mid]
        elif total<target:
            right=mid-1
        else:
            left=mid+1
    if left==right and total<target :
        new_list=list(range(0,arr[mid]+1))
        return geun_search(new_list,target)
    elif left==right and total>target:
        new_list=list(range(arr[mid],arr[mid+1]+1))
        return geun_search(new_list,target)



        
n,m = map(int,input().split()) # n은 나무 갯수 , m은 상근이가 가져가야하는 최소 나무

tree_list=sorted(map(int,(input().split()))) # 존재하는 나무 길이 받기

print(geun_search(tree_list,m))


'''

'''
다 틀림 ... 잘못생각함

그냥 받아온 리스트 중에서 가장 큰 나무의 값을 찾은 다음에 
0부터 가장 큰 나무의 값 사이에서 target값과 이분탐색을 하면됨
바보같앙 괜히 복잡하게 생각하뮤 

if total>=target? ...

'''

def geun_searh(arr,target):
    left,right=0,max(arr) #초기 인덱스 설정
    #아예 max값을 리스트의 최댓값으로 설정

    while left<=right: 
        mid=(left+right) // 2
        total=sum((x - mid) for x in arr if (x-mid) > 0 )

        if total >= target:
            result = mid
            left=mid+1
        else:
            right=mid-1
    return result




n,m=map(int,input().split())
tree_list=list(map(int,input().split()))

print(geun_searh(tree_list,m))













