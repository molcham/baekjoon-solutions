'''
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 
반올림하여 소수점 셋째 자리까지 출력한다. 
정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.


5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91


40.000%
57.143%
33.333%
66.667%
55.556%

num = 3.141592
print("{:.3f}".format(num)) 소수점 3자리 까지 출력

'''


over_list=[]
answer_list=[]
case = int(input(""))

for z in range(case):
    '''size=int(input(""))
    answer=list(input().strip())'''
    size, answer = input().split(maxsplit=1) # 띄어쓰기로 구분할 때 
    size = int(size)  # 숫자로 변환
    answer = list(map(int,answer.split()))  # 문자열을 리스트로 변환시 split 써주기
    answer_list.append(answer)

for answer in answer_list:
    over=0
    avg=0
    total=0 #오류 4번 처음에 초기값 설정해줘야함

    for k in range(0,len(answer)):
        total+=answer[k]
    avg=total/len(answer) #각 케이스 마다 평균내주기
    for z in range(0,len(answer)):
        if answer[z]>avg:
            over+=1  # 각 케이스마다 평균보다 넘는 사람 계산
        over_avg=((over/len(answer))*100) #평균 넘는 사람 비율
    over_list.append(over_avg)

for over_high in over_list:
    #print("{:.3f}".format(num)) 소수점 3자리 까지 출력
    print("{:.3f}%".format(over_high))

#오류 1번 k 위에서 썼으면 아래는 다른 변수(z) 써주기
#오류 2번 평균보다 초과 인데 이상이라 생각했음
#오류 3번 avg보다 큰걸 해야하는데 total보다 큰걸로함
#sum() 은 파이썬 내장함수라서 총합은 다른이름의 변수로 저장해주는게 좋음

        







