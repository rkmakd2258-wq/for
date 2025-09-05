# 문자 리스트 생성
lis = [ 'a','b', 'c','d', 'e']

# for문으로 리스트 요소를 하나씩 출력하기
# for 변수 in 자료구조(리스트, 튜블 등)
for ch in lis:
    print(ch)

# while문과 for문의 차이
# while : 조건을 만족하는 동안 실행
# for : 자료구조(리스트, 튜플 등)을 '순회'

# 딕셔너리 생성
# key:value
# 키는 과일이고 값은 가격인 과일 목록을 생성
dic = { 'apple':1200, 'banana':800, 'orage':1500 }

# for문으로 딕셔너리의 요소를 하나씩 출력
for key in dic:
    print(key)

# for문으로 딕셔너리의 키와 값 모두 꺼내기
print(dic.items())
print(dic.keys())
print(dic.values())


# 딕셔너리 안에 모든 아이템 꺼내기
items = dic.items()
print(items)
# 딕셔너리 안에 요소 하나씩 꺼내기 -> tuple ('apple', 1200)
for t in items:
    print(t)
#튜플을 키와 값으로 분리하기 (구조분해)
for key, value in items:
    print(key, value)


# 튜플 만들기
t = ('apple', 1200)
# 튜플 분해하기
a, b = t
print(a,b)

# for문 구조
# for 변수 in 자료구조, dict_items, dict_keys, dict_values

# 딕셔너리 안에 값만 꺼내기
values = dic.values()
print(values)
# 값 하나씩 출력하기
for value in values:
    print(value) 


# interable : 순회가 가능한 객체
# 예) dict_items, dict_keys, dict_values

# for문의 구조
# fot 변수 in 자료구조 또는 interable

#이해를...못했어.....이해를.....할 시간이 없었어.........
