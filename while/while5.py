# 반복문으로 1부터 10까지 출력하기
# 단, 숫자가 짝수일 때만 출력하기 => 홀수는 생략
#break는 중지, continue는 스킵

i = 1
while i <= 10 :
    if i%2 == 1:   #while문 안에서 continue를 만나면 
        i = i+1    #더이상 아래 코드를 실행하지 않고
        continue   # 다시 반복문으로 돌아간다
    print(i) 
    i = i+1
