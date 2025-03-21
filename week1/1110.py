'''

족보 문제 
더하기 사이클

필요할 것 같은거

1.숫자와 문자를 넣을 리스트
2.사이클 수를 구할 변수

계속 패턴을 그려보니까 반복됨
재귀함수 써주기? 
=>재귀함수 틀림 항상 메모리나 시간 관련 이슈있을때는
=>재귀함수를 어떻게 반복문으로 바꿀지 생각해보기 

count 는 함수 밖에서 선언해주고 
함수 안에서는 global 변수 전역변수로 선언해서 쓰기

함수가 한번실행 될 때 +1해주기 


def count_cycle(c,k):
    count=c
    if k<10:
        change="0"+str(k)
    else:
        change=str(k)
    
    my_list=list(change) # 리스트로 분활해주기
    hap=int(my_list[0])+int(my_list[1])
    my_list.extend(str(hap))

    new=my_list[1]+my_list[len(my_list)-1]
    if int(new)==k:
        count+=1
        return count
    else:
        count+=1
        return count_cycle(count,int(new))


n =int(input())

print(count_cycle(0,n))


'''


#함수 생성 해주기 


def count_cycle(n):
    original = n  # 처음 입력받은 숫자 저장
    count = 0  # 사이클 횟수 반복문 밖에서 선언해줘야 함 

    #count 변수는 반복문 밖에서 설정해주기

    while True:
        if n < 10:  
            n = int("0" + str(n))  # 1의 자리 수일 경우 앞에 0 추가
        
        digit_sum = sum(map(int, str(n)))  # 각 자리 숫자 합 구하기
        new_number = int(str(n % 10) + str(digit_sum % 10))  # 새로운 숫자 생성
        #10으로 나눈 나머지 즉, 1의 자리 수 끼리 더해주기 
        #만약 10의 자리끼리 더할때는 몫만 정수로 구해주는 // 사용해주기
        
        count += 1  # 횟수 증가
        if new_number == original:  # 원래 숫자로 돌아오면 종료
            return count
        
        n = new_number  # n 갱신 후 다시  while문 다시 반복
        #반복하는 조건은 항상 if문이랑 같은 위치에 

# 입력 및 실행
n = int(input())  
print(count_cycle(n))  










