import sys

input=sys.stdin.readline

n=int(input())
cards =set(map(int,input().split())) # 리스트 대신 set으로 저장 존재하는지만 check
m=int(input())
checks=set(map(int,input().split()))

for check in checks:
    print(1 if check in cards else 0, end = ' ')