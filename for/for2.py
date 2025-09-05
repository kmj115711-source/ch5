# range : 연속된 숫자를 만들어주는 함수
# 반환값 : 숫자를 담고 있는 range 객체 
# 10부터 20까지 연속된 숫자들을 반환 (마지막 숫자는 반환x)

nums = range(10,21)  #시작,끝
print(nums)

# 사용방법
for n in nums:
    print(n)

# 0부터 9까지 연속된 숫자 10개를 반환
nums=range(10)
# range객체를 사용해 "안녕하세요" 10번 출력
# range의 값이 필요하지 않은 경우(생략은 _ 언더바로 대체)
for _ in nums :
    print("안녕하세요")

# input : 키보드를 통해 값을 입력받는 함수
 #사용자가 값을 입력할때까지 대기
sum=0
# 숫자 입력받고 sum에 더하기
num1 = input()
sum = sum+int(num1)
num2 = input()
sum = sum+int(num2)
num3 = input()
sum = sum+int(num3)

# 반복문으로 숫자 3개 입력받고 합 구하기
# for문 : 반복횟수가 명확한 경우 
for _ in range(3):
     num = input()
     sum = sum+int(num)
     
print('합계:',sum)

# while문 : 조건이 명확하지 않은 경우
i =0
while i<3:
    pass
i+=1