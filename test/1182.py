from itertools import*
#n은 test케이스의 갯수수
n,s=map(int,(input().split(" ")))
my_list=list(map(int,input().split(" ")))


answer=0

for i in range (n):
    new_list=list(combinations(my_list,i+1))
    for j in range (len(new_list)):
        hap=sum(new_list[j])
        if s==hap:
            answer=answer+1

print(answer)




    




