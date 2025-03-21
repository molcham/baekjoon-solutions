'''
n이 소수인지 판단하는 가장 단순한 방법은 
2~루트n

방법 1.math.sqrt(x) => x의 제곱근을 반환 한다.
방법 2. **0.5 연산자 사용하기 (제곱근 으로 표현하기)

cmath.sqrt(-16) :복소수 루트	

오류1. my_list=list(map(int,input().split()))

map객체는 리스트 처럼 list[i] 로 인덱싱할 수 없음
=> list(map(...)) 으로 변환해줘야 인덱싱가능능

list(map())은 정수 리스트임 중요하다!!!

1은 소수 아님

for이 2번 사용되었으니까
=> 중첩된 for문안에서 약수의 갯수 --- 1번 count
=> 소수의 갯수 ---2번 count

오류 2. 소수는 자기 자신과 1을 포함 
즉 count를 통해 약수의 갯수를 찾으려면 

*판별 range 범위를 1부터 시작해야됨*

'''
import math
case=int(input())

my_list=list(map(int,input().split()))

count=0 
total_count=0

for i in range(case):

    if my_list[i]<2:
        continue


    count=0


    for k in range(1,int(math.sqrt(my_list[i])+1)):
        if (my_list[i]) % k == 0:
            count+=1 #약수 갯수 +1
            if (k*k)!=my_list[i]: 
     #제곱수가 아닌경우 쌍으로 존재하기 때문에 한번 더 +1 
                count+=1

    if count==2:
        total_count+=1  #만약 약수의 갯수가 2개 라면!
            
        
print(total_count)

    
    
    




