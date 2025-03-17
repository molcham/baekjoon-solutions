
answer=[]
case=int(input("")) #케이스 갯수 받기


for i in range(case):
    l,s=input().split(maxsplit=1) #띄어쓰기로 구분하기
    l=int(l) #몇번 반복할지 받기
    s=list(s.strip()) #어떤 문자 반복하는지 받기
    answer_list= "".join([s[k] * l for k in range(len(s))])
    '''문자열 l번 반복 후 새로운 문자열 생성해주기
    리스트 컴프리헨션과 문자열 조인을 활용한 문자 반복 코드

    리스트 컴프리헨션 [s[k] * l for k in range(len(s))]

    => s[k] * l은 k번째 문자를 l번 반복한 문자열을 생성
    => 이러한 문자열들이 리스트에 저장됨

    s배열의 k번째 (k<l) 글자 l번 반복 k가 s의 글자수보다 
    작을동안은 반복해주기

    "".join([. . .]) => 리스트를 문자열로 반환
    '''
    answer.append(answer_list)

for z in answer: #오류 1 z와 answer의 자료형은 같아야 함
    print(z)


'''
case = int(input())

for i in range(case):
    R, S = input().split()
    
    P = ""
    for i in range(len(S)):
        P += S[i] * int(R)
    
    # print("".join(map(str, P)))
    print(P)

'''

'''
s = "abc"

print(s[0])  # 'a'
print(s[1])  # 'b'
print(s[2])  # 'c'

파이썬에서의 문자열은 리스트처럼 동작하지만, 
불변객체 이므로 수정은 불가능하다!  

'''


    





'''

l=int(l)
s=list(s.strip())

for i in range(case):

for k in range(len(s)):
        print(s[k]*l,end="")

함수로도 풀 수 있지 않을까 하는생각,,,

'''


