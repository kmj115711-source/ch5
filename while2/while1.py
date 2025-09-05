# 반복문 없이 1부터 10까지 출력하세요
# i가 0부터 9까지 1씩 증가하면서 총 10번 반복수행

i= 1
while i <11:
    print(i)
    i+=1

# 반복문 없이 "안녕하세요"를 5번 출력하세요

i =0
while i < 5:
    print("안녕하세요")
    i+=1

# 반복문으로 "반가워요"를 3번 출력하세요

i =0
while i < 3:
    print("반가워요")
    i+=1


# 반복문 없이 2 4 6 8 10 짝수 5개를 출력하세요

i = 0
while i <5 :
    print((i+1)*2)
    i+=1

# 반복문으로 숫자 3부터 6까지 출력하세요

i=3
while i <= 6:
    print(i)
    i+=1


# 반복문으로 "hello"을 5번 출력하세요
i = 0 
while i <5:
    print("hello")
    i +=1

# 반복문으로 숫자 1부터 7까지 출력하세요
i = 1
while i <=7:
    print(i)
    i+=1


# 반복문으로 1 3 5 7 9 홀수 5개를 출력하세요

i = 0
while i < 5:
    print(i*2+1)
    i+=1



# 반복문을 사용해서 11부터 20까지 출력하세요
i = 11
while i<21:
    print(i)
    i+=1


# 반복문을 사용해서 1부터 5까지의 합을 출력하세요
sum = 0
i = 0

while i < 6:
    sum = sum+i
    i+=1
print("합",sum) 

# 반복문으로 리스트의 요소를 하나씩 출력하세요
nums = [10,20,30]

i =0
while i < 3:
    print(nums[i])
    i+=1


# 1부터 20까지 더한 합 구하기
# 합이 100을 넘으면 반복문을 종료
sum = 0
i = 1

while i <=20:
    if sum>100:
        break
    sum =sum+i
    i+=1
print('합계',sum) #105

# 반복문으로 요소를 하나씩 출력하다가
# 77을 만나면 break를 사용해 반복문을 종료하세요
lis = [100,77,-5,10]

i =0
while i <4:
    if lis[i] == 77:
        i+=1
        break
    print(lis[i])
    i +=1

# 1부터 10까지 하나씩 출력하다가
# 3의 배수를 만나면 break를 사용해 반복문을 종료

i = 1
while i <=10 :
    if i%3 == 0:
        break
    print(i)
    i+=1


# 반복문으로 요소를 하나씩 출력하다가
# 문자열의 길이가 4를 넘으면 반복문을 종료하세요
lis =['aa','bbb','cccc','dd']

i = 0
while i <4:
    if len(lis[i]) == 4:
        break
    print(lis[i])
    i+=1


# 반복문으로 1부터 10까지 출력하세요
# 짝수는 건너뛰고, 홀수만 출력하세요
i =1
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1




# while문으로 리스트의 요소를 하나씩 출력
# 단, 숫자를 만나면 continue를 사용해 건너뛰세요
# 리스트 생성
lis=[10,'a',True,20,'b']
i = 0
while i < 5 :
    if type(lis[i]) == int  :
        i+=1
        continue
    print(lis[i])
    i+=1