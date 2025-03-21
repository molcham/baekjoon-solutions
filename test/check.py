from itertools import combinations

n , s = map(int, input().split())


arr = []
for _ in range(n+1): 
    arr.append(int(input()))

'''

오류 1 

for문안에서 입력받으면 문제에서 요구한 것 처럼
한줄에 입력받을 수가 없어요 이건 여러줄로 입력받는 코드같습니다

arr = list(map(int, input().split()))  # 한 줄에서 입력받아 리스트로 변환
이렇게 구현하시면 split이 공백을 기준으로 나눠주고 
map이 int형으로 각 list안에 인덱스에 쪼갠 글자들을 넣어줍니다.


'''

count = 0

for i in range(n+1):  
    '''
    오류 2

    range정하실때 총 n개를 받아야 하는거면 for i in range(n)으로 해주셔야
    i 가 0부터 시작해서 n-1까지 받기 때문에 n개 받을 수 있어요
    
    '''
    subarr = []
    for j in combinations(arr, i):
        if sum(subarr[j]) == s:
            count += 1     
print(count)