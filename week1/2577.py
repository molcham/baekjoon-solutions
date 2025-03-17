answer_list=[]
a=int(input(""))
b=int(input(""))
c=int(input("")) #한줄씩 출력받기


v=str(a*b*c) # 오류4 v는 숫자임 map써주려면 str로 변경해주기

my_list=list(map(int,v)) 
'''
v=str(a*b*c)

my_list=list(map(int,v.split()))

v.split() 기본적으로 공백을 기준으로 문자열을 나누는데
곱한 결과 a*b*c는 공백이 없기때문에 아무런 효과가 없다

map() 함수는 반복가능한 객체(리스트,문자열,튜플) 의
각 요소에 함수를 적용하여 새로운 값을 반환하는 함수이다.

map(int, some_string) :각 문자 단위로 변환 (공백 기준 X)
['1', '2', '3'] → [1, 2, 3]

'''
#오류 1total_number=0  여기다가 해주면 숫자마다 초기화가 안돼서 누적됨

for i in range(10): #오류2 :0부터 9 니까 10개라서 그냥 아예 입력하기
    total_number=0 # 오류3 : 숫자마다 초기화해주어야 올바르게 판별가능능
    for k in range(0,len(my_list)):
        if i==my_list[k]:  #만약 숫자 i와 리스트안의 숫자가 같다면 
            total_number+=1 #일치하는 토탈갯수 1증가
    print(total_number) #각 숫자마다 일치하는 숫자갯수 출력
        





'''
answer = list(map(int,answer.split()))  # 문자열을 리스트로 변환시 split 써주기
answer_list.append(answer)
'''

