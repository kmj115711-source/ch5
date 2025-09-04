# 반복문으로 1부터 20까지 합 구하기
# 단, 합이 100을 넘으면 while문을 중단

sum = 0
i=1
while i <= 20 :
    sum = sum + i
    if sum > 100:
        print('마지막 sum:',sum)
        print('마지막 i:',i)  # while문 안에서 break를 만나면
        break                # 반복횟수가 끝나지 않았어도 while문 중단
    i+=1
print(sum) #마지막sum : 105, 마지막i :14