'''

스택 문제...
(())() => 문자열임
((()))(()) => 문자열임
()()()()()( =>문자열 아님 

스택의 push와 pop을 이용


'''

#그냥 한줄 씩 출력하면됨
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    command = sys.stdin.readline().strip()
    stack = []
    for i in command:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack):
        print('NO') #만약 스택에 문자가 남아있으면 짝이 안맞는거임 => 고로 문자열이 아님 
    else:
        print('YES') # 만약 스택에 문자가 남아있지 않으면 짝이 맞아서 모두 지워진거임 => 고로 문자열열

             



















