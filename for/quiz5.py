# 다음과 같이 학생 점수 딕셔너리를 만들어주세요
scores={ "철수":80, "영희":95, "민수":70, "지연":100 }

# # for 문을 사용해 전체 평균 점수를 구하세요
# sum =0

# #총점구하기
# for v in scores.values() :
#     sum=sum+v
#     print("합계:", sum)

# # 학생의 수 구하기
# size = len(scores)

# # 평균 구하기
# avg = sum / size
# print(avg)  # 86.25


# for 문을 사용해 90점 이상 학생의 수를 구하세요

# 90점 이상 학생의 수를 구하세요

# 학생의 수를 저장할 변수
cnt=0

# 80 95 70 100 중에서 90보다 큰 점수 찾기
for value in scores.values():
    if value >= 90:
        print(value)  #95 100
        cnt =cnt + 1
print('학생의 수 :', cnt)        #학생의 수 : 2
# 조건을 만족하는 학생을 찾으면 cnt를 1만큼 증가

