scores = {'철수':80, '영희':95, '민수':70, '지연':100}
# for문을 사용해 전체 평균 점수를 구하세요
# 1. 총점 구하기
sum = 0 #총점을 저장할 변수
# values는 이터러블로 for문 사용 가능
for value in scores.values():
    # 누적, 합 구하는 공식
    sum = sum + value
print('합계:', sum)

# 2. 학생수 구하기
print(len(scores))
size = len(scores)

# 3. 평균 구하기
avg = sum / size
print(avg)


# for문을 사용해 90점 이상 학생의 수를 구하시오
# 학생의 수를 저장할 변수
cnt = 0
for value in scores.values():
    if value >= 90: # 학생의 점수와 90을 비교
        print(value)
        cnt = cnt + 1
print('학생의 수:', cnt)


