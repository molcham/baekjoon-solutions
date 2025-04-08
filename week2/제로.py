'''
첫줄 : 정수 k가 주어짐

정수가 0일 경우: 가장 최근에 쓴 수를 지운다
+지울 수 있는 수가 있음을 보장할 수 있다.

0이면 pop해주기
아니면 push 하기

'''

k=int(input())

my_list=[]

for i in range(k):
    money=int(input())
    if money!=0:
        my_list.append(money)
    else:
        my_list.pop()
total=sum(my_list)

print(total)





