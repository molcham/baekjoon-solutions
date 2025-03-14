n=int(input())

#ㄱ+한자키가 다양한 기호임 
  

#(1,10)으로 range빼먹고 입력하면 그냥 1이랑 10만 나옴 바보야!!!
for i in range(1,10):
    (print(str(n) + " * " + str(i) + " = " + str(n * i)))
    i += 1


