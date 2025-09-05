# 다음과 같이 리스트를 만들고
# for 문으로 요소를 하나씩 출력하세요
mixed = [1,"apple", 3.14, True]

# for 변수 in 자료구조 (list tuple dic iter)
for m in mixed:
    print(m)


fruits = ["apple", "banana", "cherry"]

for f in fruits:
    print(f)


students = {"이름":"둘리", "나이":20, "주소":"인천"}

for key in students:
    print(key)
#for 변수 in iter
for value in students.values():
    print(value)

coffee_menu = {"아메리카노":"2500원", "라떼":"3000원", "케이크":"4500원"}

for value in coffee_menu:
    print(value)

 

nums = range(11, 21)

for n in nums:
    print(n)

nums = range(5, 16)

for n in nums:
    print(n)

nums = range(5)
for _ in nums:
    print('hi')


nums = [10,20,30,40,50]
sum = 0 #합을 저장할 변수
#for 변수 in 자료구조(리스트)
for n in nums:
    sum = sum+n #누적코드
print('합계:', sum)


nums = range(1,101)
for n in nums:
    if n%3 == 0:
        print(n) 


num=5
#문자열 반복 연산
print('*'*num) 

#for문 
str1 = ''
for _ in range(num):
    str1 = str1  + '*'
print(str1) 

# n의 크기만큼 삼각형을 그려주세요
# n=5
n = 5
for i in range(1,n+1):
    print(' ' * (n - i) + '*' * i)



# 구구단 중에서 3단을 출력하세요
n=3
for i in range(1,10):
    print('3 X',i,'=', n*i)


