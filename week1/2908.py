'''
문자열 뒤집는 연산 사용 

s[::-1] ⇒ 문자열 뒤집기

'''

a,b=map(str,input().split())

#문자열 뒤집기
a=int(a[::-1]) 
b=int(b[::-1]) 

if a>b:
    print(a)
else:
    print(b)