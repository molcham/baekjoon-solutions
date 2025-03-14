x,y,w,h=(input().split()) #input() 은 항상 문자열로 입력받음


x=int(x)
y=int(y)
w=int(w)
h=int(h)

# map() 함수 써주기 나뉜 문자열을 정수로 반환해주는 함수

if (x<=(w/2)) and (y>(h/2)):
    print(int(min(x,h-y)))
elif (x>(w/2)) and (y>(h/2)):
    print(int(min(w-x,h-y)))
elif (x<=(w/2)) and (y<(h/2)):
    print(int(min(x,y)))
elif (x>(w/2)) and (y<(h/2)):
    print(int(min(w-x,y)))
else:
    print(int(min(w/2,h/2)))




#짧은 답
#x,y,w,h = map(int,input().split())
#print(min(min(w-x,x),min(h-y,y)))

# min(w-x,x) = x와 w-x 중에 더 작은 값 (가로 방향 최단 거리)
# min(h-y,y) = y와 h-y 중에 더 작은 값 (세로 방향 최단 거리)
# min(가로방향 최단거리,세로방향 최단거리) => 최종적으로 가장 짧은 거리 선택








