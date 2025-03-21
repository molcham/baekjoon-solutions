#new=sum(int(str(original).split())) #2글자로 나눔,두 글자 더함
#자꾸 입력만 받고 출력은 렉걸림 ㅗㅗ

def count_number(k):

    count=0

    original=k


    while True:


        if original<10:
            original=int('0'+str(original))
            
        #new=sum(int(str(original).split())) #2글자로 나눔,두 글자 더함
        tmp_list=[str(original)[0],str(original)[1]]
        
        new=int(tmp_list[0])+int(tmp_list[1])
        
        next_number=int(str(original%10)+str(new%10))

        count=count+1

        if int(next_number) == k: 
            '''
            original이 아니라 k랑 비교해줘야됨 
            orgianl은 계속 변하기 때문에 비교대상이 될 수 없다.
            '''
            return count
        
    
        original=next_number # next_number =origianl은 무한 루프 발생 

n=int(input())

print(count_number(n))

