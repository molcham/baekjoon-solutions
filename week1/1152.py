'''

공백을 기준으로 새야하지 않을까,,,

split() 은 연속된 공백을 하나의 구분자로 처리
=> 단어만 리스트에 저장할 떄 

split(" ") 모든 공백(스페이스 한칸만) 기준으로 나눈다
=>빈 문자열도 리스트에 저장한다 

input()은 기본적으로 문자열로 받음음

다른사람 짧은 코드

s = input() 
print(len(s.split()))


'''

my_list=input("").split()

l=len(my_list)

print(l)



