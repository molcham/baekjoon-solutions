# 영어 o/x대문자로 입력함
#첫번째 인덱스일때와 아닐때로 구분해줘야 하나....

score=0
sum=0
scores=[]
answer_list=[]

i=int(input(""))
for z in range(i):
    answer=list(input().strip())
    answer_list.append(answer)


for answer in answer_list:
    score=0
    sum=0

    for k in range(0,len(answer)): #k는 명시적으로 +1 안해줘도 늘어나용용
        a=answer[k]
        if k==0:  #첫번째 인덱스 일때 앞에 O없음 
            if a=='O':
                score+=1 #0에서 1로 증가시켜주기
                sum+=score
            else:
                score=0 #첫번째가 X일때 
                sum+=score
        else:  #첫번째 인덱스 아닐때 앞에 요소가 있을때 
            if a=='O': #해당 인덱스가 O일때는 앞에 O가 몇개인지가 중요해짐
                if answer[k-1] == 'O': #바로 앞의 인덱스가 O이면 
                    score+=1 #score 누적해서 증가시켜주기
                else:
                    score=1 #해당인덱스는 O이지만 앞의 인덱스의 요소가 X라서 다시 1부터 시작
                sum+=score #해당인덱스 체크하고 score초기화시켜준뒤 누적
            else:
                score=0 #해당 인덱스가 그냥 애초에 X일때 
    scores.append(sum)  # 해당 줄에대한 sum값 저장


for sum in scores:
    print(sum) #모든 케이스에 대한 결과값 한줄씩 출력해주기
            



'''
answer=list(input().strip())
for k in range(0,len(answer)):
    answer=list(input().strip())
    a=answer[k]

    if k==0:
        if a=='O':
            score+=1
            sum+=score
        else:
            score=0
            sum=0
    else:
        if (a=='O') and answer[k-1]=='O':
            score+=1
            sum+=score
        elif (a=='O') and answer[k-1]!='O':
            score=1
            sum+=score
        else:
            score=0
            sum+=score
'''
"""my_list=[0]*9
for i in range(9):
    k=int(input(""))
    my_list[i]=k

a=my_list[0]
for z in range(8):
    a=my_list[0]
    if my_list[z]>a:
        a=my_list[z]

print(a)
print((my_list.index(a))+1)"""

'''i=int(input(""))

for k in range(0,i):
    a,b=map(int,input().split())
    print(f"{a+b}")
    k+=1 '''

'''

i=int(input(""))
score=0
sum=0
answer=[]

for z in range(i):
    answer=list(input().strip())
    for k in range(0,len(answer)):
        answer=list(input().strip())
        a=answer[k]
        if k==0:
            if a=='O':
                score+=1
                sum+=score
            else:
                score=0
                sum=0
        else:
            if (a=='O') and answer[k-1]=='O':
                score+=1
                sum+=score
            elif (a=='O') and answer[k-1]!='O':
                score=1
                sum+=score
            else:
                score=0
                sum+=score

print(sum)

'''