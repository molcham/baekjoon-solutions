'''

왼쪽기준으로 부딪히는 탑이 있으면
몇번째 탑인지 출력하기

없으면 0 출력하기

스택 사용하기 

인덱스 0부터 차례로 확인



'''
'''
for문으로 하면 시간 초과난다.
시간초과 안나려면 스택 사용해야함 
import sys

def find_top(arr,n):
    result=[]
    #맨 끝 원소부터 확인하면서 큰 원소 append하기
    for i in range(n): #n-1부터 0까지 탐색 
        x=next((j for j in range(i-1,-1,-1) if arr[j]>arr[i]),-1)
        #조건을 만족하는 인덱스 j를 반환
        result.append(x)
    final_result = [x + 1 for x in result]
    return final_result #원래 순서로 맞춰서 반환

n=int(sys.stdin.readline()) #몇개의 탑 입력받을지 
top_list=sys.stdin.readline().split() #입력 받아서 스택에 저장

print(find_top(top_list,n))

'''
import sys
input = sys.stdin.readline

n=int(input())

towers=list(map(int,input().split())) #list로 생성해주기

stack=[]
result=[0]*n

for i in range(n): # 1번 부터 n번 탑까지 탐색
    while stack:
        if towers[i]>towers[stack[-1]]:
            #만약 내가검사하는 타워가 stack에 있는 타워보다 크다면
            stack.pop()
        else:
            #만약 내가검사하는 타워가 stack에 있는 타워보다 작거나..
            #스택이 비어서 더 이상 확인할 탑이 없다?
            #result에 나보다 큰 탑의 towers에 있는 인덱스 넣어주기
            result[i]=stack[-1]+1 #가장 최신의 탑
            #stack은 인덱스 값이니까 +1해서 몇번째 탑인지 저장 
            break
    stack.append(i)

print(*result) 







    





    








    






