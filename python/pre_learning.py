#문자열 포맷팅
a = 5
b = 3

print('{0} + {1} = {2}'.format(a, b, a + b))
#대충 이런 느낌

#f를 이용한 포매팅
name = input('당신의 이름을 입력하세요: ')
age = input('당신의 나이를 입력하세요: ')
print(f'이름: {name}, 나이: {age}')