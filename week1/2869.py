'''
재귀함수 호출?

입력받은 값을 바로 함수 호출하면서 전달하는 방법

함수에 직접 전달

def add(a , b):
  return a+b

result = add (*map(int, input().split()))

*map(...) : 변환된 값을 개별 인자로 풀어서 함수로 전달
* 는 언패킹 연산자, 이를 통해 함수에 여러 인자를 전달할 수 있음 

print(result)

오류 시간초과! => 반복문이나 재귀함수 호출은 안됨 오래걸림 ㅜㅜㅜ

'''

#a,b,v=map(int,input().split())



'''def snail(a,b,v):
    day=0
    v=v-a+b
    if v>0:
        day+=1
        snail(a,b,v-a+b)
    return day



    맞는 함수

    def snail(a,b,v):
    if v<=a:
        return 1
    return 1 +snail(a,b,v-a+b)

    print(snail(*map(int, input().split())))


    재귀함수말고 반복문으로 바꿀때

    def snail_iter(a, b, v):
    day = 0
    while v > 0:
        day += 1  # 하루 경과
        v -= a    # 낮에 a만큼 올라감
        if v <= 0:
            break  # 목표 높이에 도달하면 종료
        v += b    # 밤에 b만큼 미끄러짐
    return day

    # 입력받아 실행
    print(snail_iter(*map(int, input().split())))

    '''

'''
def snail(a,b,v):
    if v<=a:
        return 1
    return 1 +snail(a,b,v-a+b)

print(snail(*map(int, input().split())))

마지막날에 정상에 도착하면 미끄러지지 않으므로 
올라가는 것만 생각해서 식을 새우면 
총 올라가야하는 거리는 v-a이다.
하후에 실제 이동하는 거리는 a-b이다.


'''

a,b,v=map(int, input().split())

day=0

if v<=a :
    day=1
else:
    if (v-a) % (a-b) ==0:
        day=(v-a)/(a-b)+1 #+1은 첫날 올라간거거
    else:
        day=(v-a)/(a-b)+2 #첫날 올라간거 + 나머지 있어서 올라간거

print(int(day))
    






