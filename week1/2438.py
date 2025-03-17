i=int(input())

for k in range(1,i+1):    # 1번째 줄에는 1개 이니까 0부터 시작하면 안됨! 
    for j in range(0,k):
        print("*",end="")
        j+=1
    print()     #print()는 줄바꿈 해줌!
    k+=1
        
