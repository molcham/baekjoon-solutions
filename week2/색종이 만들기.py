'''
n = int(input())

tree = [list(map(int,(input()))) for _ in range(n)]
print(tree)
result = []

def quad_tree(x,y,n):
    global result
    color = tree[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]: # 범위안에 한개라도 다른경우는 4분면으로 나눠서 다시 검색
                result.append("(") # 4분면으로 나눌때 괄호를 친다.
                quad_tree(x,y,n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(color) # 재귀로 안들어가고 for문이 전부 다 끝난 상태이기 때문에 범위안에 모든수가 같다고 볼 수 있다.

quad_tree(0,0,n)
print("".join(map(str,(result))))

'''

#재귀 + 분할 정복

cut=[]

#result=1

white_count=0
blue_count=0
#함수 밖에서 선언 해주기

def cut_paper(x,y,n):
    #global result
    cut=paper[x][y] #좌표처럼 설정해주기 cut이라는 2차원 리스트 생성

    global white_count
    global blue_count  #함수밖에서 선언한 변수들 전역변수로

    if all(paper[i][j] == cut for i in range(x, x+n) for j in range(y, y+n)):
        if cut == 1:
            blue_count += 1  # 파란색 색종이 증가
        else:
            white_count += 1  # 흰색 색종이 증가
        return  # 더 이상 나눌 필요 없음
    
    '''
    내가 실수한 부분: for문안에 아래의 재귀함수 호출 부분을 넣어버림 
    for문안에 넣으면 '각 칸을 검사할 때 마다 재귀호출이 실행됨'

    색이 다른 칸이 발견될 때마다 4개의 재귀 호출이 발생하는 비효율적인 코드가 된다.

    '''

    
    #위의 for문안에 이걸 넣으면 안됨!...
    #result=result-1+4
    cut_paper(x,y,n//2)
    cut_paper(x,y+n//2,n//2)
    cut_paper(x+n//2,y,n//2)
    cut_paper(x+n//2,y+n//2,n//2)
                

            


n=int(input())
paper=[list(map(int,(input().split()))) for _ in range(n)]

cut_paper(0,0,n)

print(white_count)
print(blue_count)

