'''
각 자리수끼리의 차가 같은거 ??

오름차순 내림차순 생각해주면 절댓값씌워주기

0~1000까지임

len(s)=문자열의 길이 

s.split() 해서 리스트에 넣어주기 

*abs(n) => n의 절댓값 반환해준다

101안됨 111됨 123됨 
만약 특정 숫자보다 아래있는애가 수가 다 같으면 가능

1.같거나 
2.1의자리<10의 자리<100의 자리거나
3.1의자리>10의 자리>100의 자리

0~99



for k in range (100,s+1):
            ex_list=list(str(k))

            a = abs(int(ex_list[2]) - int(ex_list[1]))
            b = abs(int(ex_list[1]) - int(ex_list[0]))


'''
'''s=int(input())
i=len(str(s))

ex_list=[]
count=0






if s==1000:
    print(144)
else:
    if i==3:
        for k in range (100,s+1):
            ex_list=list(str(k))
            if int(ex_list[0])>int(ex_list[1]) and int(ex_list[1])>int(ex_list[2]):
                a = abs(int(ex_list[2]) - int(ex_list[1]))
                b = abs(int(ex_list[1]) - int(ex_list[0]))
                if a==b:
                    count+=1
                else:
                    break
            elif int(ex_list[0])<int(ex_list[1]) and int(ex_list[1])<int(ex_list[2]):
                a = abs(int(ex_list[2]) - int(ex_list[1]))
                b = abs(int(ex_list[1]) - int(ex_list[0]))
                if a==b:
                    count+=1
                else:
                    break   
            elif int(ex_list[0])==int(ex_list[1]) and int(ex_list[1])<int(ex_list[2]):
                count+=1
            else:
                break
        print(100+count)

    else:
        print(int(s))
'
'''

s = int(input())  # 입력 받기
count = 0  # 한수 개수 카운트

if s == 1000:
    print(144)  # 1000은 예외 처리
else:
    if s >= 100:  # 100 이상부터 한수 개수 계산
        for k in range(100, s + 1):
            ex_list = list(map(int, str(k)))  # 숫자를 리스트로 변환
            
            # **한수 조건: 모든 숫자가 같거나, 등차수열을 이루는 경우**
            if (ex_list[0] == ex_list[1] == ex_list[2]) or \
               ((ex_list[0] > ex_list[1] > ex_list[2] or ex_list[0] < ex_list[1] < ex_list[2]) and
                (ex_list[2] - ex_list[1] == ex_list[1] - ex_list[0])):
                count += 1  # 한수 개수 증가

        print(100 + count)  # 100 이하의 모든 수는 한수이므로 100 + 추가 개수
    else:
        print(s)  # 100 미만의 숫자는 그대로 출력 (1~99는 모두 한수)
1






    




