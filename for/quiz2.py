# for 문을 사용해서 11부터 20까지 출력하세요
nums=range(11,21)
for n in nums:
    print(n)

# for 문을 사용해서 5부터 15까지 출력하세요
nums2=range(5,16)
for n in nums2:
    print(n)

# for 문을 사용해서 "hi" 5번 출력하세요
nums3=range(5)
for _ in nums3:
    print('hi')



nums = [10,20,30,40,50]
# for문으로 모든 요소를 더해서 합을 구하세요
sum = 0
for n in nums:
    sum += n
print("합:", sum)

# for문을 사용해서 
# 1부터 100까지 숫자 중에서 3의 배수만 출력하세요
for n in range(1,101):
    if n%3 ==0:
      print(n)