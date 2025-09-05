
# 리스트 생성
nums = [5,9,3,8,2]

# 리스트에서 가장 큰 값 구하기 => 9
max = nums[0] #가장 큰 값을 저장할 변수

# 과정
# max, nums[i]
# 5 9 비교 => 9 (max nums[1])
# 9 3 비교 => 9 (max nums[2])
# 9 8 비교 => 9 (max nums[3])
# 9 2 비교 => 9 (max nums[4])
# 현재 가장 큰 값, 리스트의 요소

for n in nums:
    # 현재 max의 리스트의 요소를 비교하여
    # 리스트의 요소가 더 크면 max를 교체
    if max < n:
        max = n #교체 
    print('최대값:', max) 


# for문 안에서 break 와 conrinue 쓰기
# for문으로 1부터 20까지 합 구하기
# 합이 100을 넘으면 반복문 중단
sum=0
for i in range(1,21):
    if sum > 100:
        break
    sum = sum + i # 누적 공식 코드( 자기자신 + 더하는 수 )
    print('합계:',sum) 

# for문에서 conrinue 사용하기
# continue : 건너뛰기(skip)

# for문으로 1부터 10까지 출력하세요
# 홀수는 건너뛰고 짝수만 출력하세요
for i in range(1,11):
    if i%2 ==1:
        continue
    print(i)