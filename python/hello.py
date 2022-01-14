# 변수 라는 개념
dust = 60

greeting = 'Hello, World!'

# ctrl + / -> 지정한 영역 전체주석. 한번 더 하면 취소.
# print(greeting)
# print(greeting)
# print(greeting)
# print(greeting)
# print(greeting)

# while문

count = 0
while count < 4:
    #조건을 만족하는 동안 아래의 코드 실행
    print(greeting)
    
    count = count + 1
print('while 끝남')

# for문
# 정해진 범위 안에서 반복 실행
# 범위는? 어디서 구할까

for i in range(4):
    print(greeting)
print('for문 끝남')