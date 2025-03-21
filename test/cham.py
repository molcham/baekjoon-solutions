N = int(input())  
original_N = N  
count = 0  

while True:
    a = N // 10 + N % 10  # 각 자리 숫자의 합
    N = (N % 10) * 10 + a % 10  # 새로운 숫자 생성
    count += 1

    if N == original_N:  # 원래 숫자로 돌아오면 종료
        break

print(count)
