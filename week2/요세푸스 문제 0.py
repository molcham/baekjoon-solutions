'''
큐 사용해서 풀기

 
원에서 사람들이 제거되는 순서를 (n,k)=요세푸스 순열 
n명의 사람 , k번째 사람을 제거 

n명의 사람이 모두 제거될 때 까지 계속 반복 
함수에 arr, 제거할 k번째 전해주기


'''

from collections import deque
import sys



#print(*queue)

def circle(arr,k):
    arr=list(arr)
    result=[] #선택된 k번째 저장할 리스트
    now=0
    while len(arr)>0:
        now=(now+(k-1))%len(arr)
        p=arr.pop(now)
        result.append(p)
    return result

n,k=map(int,(sys.stdin.readline().split()))

queue=deque(range(1,n+1)) # 1부터 n까지 채운 deque 생성


print("<" + ", ".join(map(str, circle(queue, k))) + ">")











    


