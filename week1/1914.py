'''
하노이탑

3개의 장대, 서로다른 n개의 원판

첫번째 줄 옮긴 횟수 K 출력

N이 20이하면 입력에 대해서 두번째 줄 부터 수행 과정 출력


만약 4개 일 때

제일 작은 수부터 end로 이동
그다음 작은 수는 middle로 이동
제일 작은 수 middle로 이동 (1번 2번 합쳐짐)

3번째로 작은 수 end로 이동
middle에 있던 제일작은수 start로 이동 
2번째로 작은 수 end로 이동
start에 있는 제일 작은수 end로 이동 (1,2,3번 합쳐짐)

4번째 middle로 이동
end에 있던 1번 start로 이동 
end에 있던 2번 middle로 이동 (4,2번 합쳐짐)
start에 있던 1번 end로 이동 (1,3번 합쳐짐) 
middle에 있던 2번 start로 이동 
end에 있던 1번 start이동 (1,2번 합쳐짐)
end에 있던 3번 middle로 이동 (4,3번 합쳐짐)
start 에 있던 1번 end로 이동
start에 있던 2번 middle로 이동 (4,3,2) 합쳐짐
end에 있던 1번 start로 이동 
middle에 있던 2번 end로 이동 
start에 있던 1번 end로 이동 (1,2번 합쳐짐) => middle엔 4,3
middle에 있던 3번 start로 이동
end에 있던 1번 middle로 이동 
end에 있던 2번 start로 이동 (3,2 합쳐짐)
middle에 있던 1번 start로 이동 (3,2,1 합쳐짐)


middle에 있던 4번 end로 이동 (이제 안움직임)
start에 있던 1번 end로 이동(1,4 합쳐짐짐)
start에 있던 2번 middle로 이동 
end에 있던 1번 middle로 이동(2,1 합쳐짐)
start에 있던 3번 end로 이동 (이제 안움직임)
middle에 있던 1번 start로 이동
middle에 있던 2번 end로 이동 (이제 안움직임)
start에 있던 1번 end로 이동(이제 안움직임)

완료료 4,3,2,1 합쳐짐

pythontutor


hanoi(3,1,2,3)
n!=1

hanoi(2,1,3,2) 원판이 2개라는 얘기잔니 

n!=1
hanoi(1,1,2,3) 원판이 1개로 줄었어 
print(1,3) 1번이 3번으로로

hanoi(2)

#제일 큰 원판 첫번째 기둥에서 마지막 기둥으로

#나머지 원판들 중간기둥으로 옮겨놨던 것들 마지막 기둥으로




'''

def hanoi(n,fr,tmp,to):
    if (n==1):
        print(fr,to)
        return
    hanoi(n-1,fr,to,tmp)
    print(fr,to)  #제일 큰 원판 첫번째 기둥에서 마지막 기둥으로
    hanoi(n-1,tmp,fr,to) #나머지 원판들 중간기둥으로 옮겨놨던 것들 마지막 기둥으로

k=int(input())
print((2**k)-1)

if k<=20:
 hanoi(k,1,2,3)

#원판의 크기가 20이하일때만 출력경로 출력하기



