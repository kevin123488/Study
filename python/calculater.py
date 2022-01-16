# #간단 계산기 만들기
# from cmath import nan

# 숫자1 = int(input("첫번째 숫자를 입력하세요: "))
# if 숫자1 != nan:
#     print('연산자를 입력하세요: ')
# else:
#     print('올바른 숫자를 입력하세요')

# 연산자 = input()
# if (연산자 != '*') and (연산자 != '+') and (연산자 != '-') and (연산자 != '/'):
#     print('올바른 연산자를 입력하세요')
# else:
#     print('잘하고 있어')

# 숫자2 = int(input('두번째 숫자를 입력하세요: '))
# if 숫자2 != nan:
#     print(f'{숫자1} {연산자} {숫자2} = 이걸 계산 못한다고?')
# else:
#     print('올바른 숫자를 입력하세요')

#구구단 코드 작성

dan = int(input("숫자 입력: "))
list = [1, 2, 3, 4 , 5, 6, 7, 8, 9]
for i in list:
    print("{0} * {1} = {2}" .format(dan, i, dan * i))