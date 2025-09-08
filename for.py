# 반복문 : while for
# while : 조건이 참인 동안 반복 수행
# fot : 자료구조에서 요소를 하나씩 꺼내면서 반복 수행

lis = ['a', 'b', 'c', 'd', 'e']
# 리스트의 크기만큼 반복 수행
# 리스트의 요소를 하나씩 꺼내서 변수에 저장 후 사용
for ch in lis:
    print(ch)

# 딕셔너리 생성
# key-value 쌍
dic = {'apple':1200, 'banana':800, 'orange':1500}

# for문으로 딕셔너리 안에 요소 하나씩 꺼내기
for k in dic:
    print(k) 

# 값 꺼내기
# 딕셔너리에서 dict_values 객체 추출
print(dic.values())

# for 변수 in 리스트, 튜플, 딕셔너리, iter
# iteralble(이터러블): 순회가 가능한 객체
for v in dic.values():
    print(v)

# dic.items : 키, 값 모두 가지고 있는 객체
# 튜플 구조 분해로 값을 하나씩 변수에 대입
for key, value in dic.items():
    print(key, value)

# range : 연속된 숫자를 만드는 객체
# range(개수)
print(range(10))

# range는 이터러블 객체
for n in range(10):
    print(n)
# range(시작, 끝)
for n in range(1,11):
    print(n)
# 안녕하세요 10번 출력
# n 변수 사용 안 함 => 변수 생략 가능
for _ in range(10):
    print('안녕하세요')

# # 리스트 생성
# nums = [1,2,3,4]
# # 새로운 리스트
# new_nums = []
# # nums를 사용해 새로운 리스트 생성
# # nums의 각 요소에 *3을 해서 [3,6,9,12] 만들기
# for n in nums:
#     # 새로운 리스트에 값 담기
#     new_nums.append(n*3)

# # 위 코드를 '리스트 컴프리헨션'이라는 문법으로 간단하게 작성하기!
# # 새로운 리스트 = [ 변수 + 반복문 ]
# new_nums = [ n*3 for n in nums ]
# print(new_nums)


nums = [1,2,3,4,5,6,7,8,9,10]
# nums를 사용해 새로운 리스트 만들기
new_nums = []
# nums에서 짝수만 골라서 new_nums에 담기
for n in nums:
    if n%2 == 0:
        new_nums.append(n)
print(new_nums)

# 위 코드를 '리스트 컴프리헨션'문법으로 바꾸기
# 새로운리스트 = [ 변수 + for + if ]
# 마지막으로 앞에 있는 n을 리스트에 추가
new_nums = [ n for n in nums if n%2 == 0 ]
print(new_nums)


# 리스트 생성
strings = ['a', 'bb', 'ccc', 'dddd', 'e']
# strings을 사용해 새로운 리스트 만들기
new_str = []
# 문자열 리스트에서 문자의 크기가 2보다 큰 것을 찾고
# 대문자로 변환해서 new_str에 담기
for ch in strings:
    # 문자의 크기가 2보다 큰 것 찾기
    if len(ch) > 2:
        print(ch, len(ch), ch.upper()) 
        new_str.append(ch.upper())
print('결과:', new_str)

# 위 코드를 '리스트 컴프리헨션'문법으로 바꾸기
new_str = [ ch.upper() for ch in strings if len(ch) > 2]
print('결과:', new_str)