#split() 은 입력값을 공백 기준으로 분리하여 리스트로 만든다!

size,i=map(int,input().split())

my_list=map(int,input().split())
answer_list=[]

for k in my_list :
    if k<i:
        answer_list.append(k)
    
print(*answer_list) #unpacking 연산자 사용하기 => list의 요소를 공백으로 구분하여 출력해줌
        





