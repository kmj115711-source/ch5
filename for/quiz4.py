# 리스트에서 가장 큰 값 구하기 =>9
#가장 큰 값을 저장할 변수
#현재 max와 리스트의 요소를 비교
#리스트의 요소가 더 크면 max를 교체

nums=[5,9,3,8,2]
max =nums[0]

for n in nums:     
        if max<n:
            max = n
print('최대값:', max)
                        
 
#  for 문 안에서 break와 continue 쓰기

# for문으로 1부터 20까지 합 구하기
#자기자신 + 더하는 수 =합, 누적 (sum = sum + i)

# 합이 100을 넘으면 반복문 중단
total = 0
for i in range(1, 21):
    if total>100:
         break
    total += i
print(' 합:', total)

# for문에서 continue사용하기
# continue : 건너뛰기

# for문으로 1부터 10까지 출력하세요
# 홀수는 건너뛰고 짝수만 출력하세요
for i in range(1,11):
     if i%2==1:
          continue
     print(i)   