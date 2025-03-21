'''
골드바흐의 추측은 유명한 정수론의 미해결 문제로,
2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.


여러개의 경우의 수가 있을 때 두 수의 차이가 가장 작은걸로 선택 
=> 나누기 2하면 되지 않을까 하는 생각 
=> 나누기 2했을 때 짝수인지 홀수인지 생각각
'''

'''import math

def is_prime(n):
    """입력된 수 n이 소수이면 True, 아니면 False 반환"""
    if n < 2:
        return False  # 1은 소수가 아님

    count = 0  # 나눠지는 횟수 카운트

    for k in range(1, int(math.sqrt(n)) + 1):  # 1부터 √n까지 확인
        if n % k == 0:
            count += 1  # 약수 발견
            if k * k != n:  # 제곱수가 아닌 경우, 약수 쌍 존재
                count += 1

    return count == 2  # 약수가 정확히 2개면 소수


    한번에 한개씩 출력해라 
    4도 오류뜸 
    '''
import math
my_list=[]
answer_list=[]

case=int(input())
my_list=[0]*case

rows,cols=case,2
matrix=[]
for i in range(rows):
    matrix.append([0] * cols)  # 각 행에 길이 cols만큼 0으로 초기화


for i in range(case):
    my_list[i]=int(input())

for k in range(case):
    if ((my_list[k]/2)%2)==0:
        m=(my_list[k])/2
        n=1
        while (m-n)>1 and (m+n)>1:
            is_prime_mn = (m-n > 1) and all((m-n) % w != 0 for w in range(2, int(math.sqrt(m-n)) + 1))
            is_prime_mp = (m+n > 1) and all((m+n) % w != 0 for w in range(2, int(math.sqrt(m+n)) + 1))

            if is_prime_mn and is_prime_mp:
                matrix[k][0],matrix[k][1]=int(m-n),int(m+n)
                #인덱스는 0부터 시작한다
                break
            n+=2
    else:
        m=(my_list[k])/2
        n=0
        while (m-n)>1 and (m+n)>1:
            is_prime_mn = (m-n > 1) and all((m-n) % w != 0 for w in range(2, int(math.sqrt(m-n)) + 1))
            is_prime_mp = (m+n > 1) and all((m+n) % w != 0 for w in range(2, int(math.sqrt(m+n)) + 1))

            if is_prime_mn and is_prime_mp:
                matrix[k][0],matrix[k][1]=int(m-n),int(m+n)
                #인덱스는 0부터 시작한다
                break
            n+=2




for row in matrix:  # 각 행을 순회
    print(" ".join(map(str, row)))  # 숫자를 문자열로 변환 후 공백으로 연결

            
                 
                 
        
        










        



        
    
    