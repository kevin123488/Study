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

# dan = int(input("숫자 입력: "))
# list = [1, 2, 3, 4 , 5, 6, 7, 8, 9]
# for i in list:
#     print("{0} * {1} = {2}" .format(dan, i, dan * i))

#인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
#이 때 1 인치는 2.54 센티미터입니다.

# num = int(input())
# num2 = num * 2.54
# print(f'{num} inch => {num2} cm')

# num = int(input())
# num2 = num * 2.54
# print('{%.2f} inch => {%.2f} cm'.format(num,num2))

# a = int(input())
# for i in range(1, a+1):
#     if a%i == 0:
#         print(f'{i}(은)는 {a}의 약수입니다.')

# a = int(input())
# count = 0
# for i in range(1, a+1):
#     if a%i == 0:
#         print(f'{i}(은)는 {a}의 약수입니다.')
#         count += 1
        
# if count == 2:
#     print(f'{a}(은)는 1과 {a}로만 나눌 수 있는 소수입니다.')

# a=int(input())
# count = 0
# for i in range(1,a+1):
#    if not (a % i) :
#           print("%d(은)는 %d의 약수입니다." % (i, a))
#           count += 1
# if count == 2:
#    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (a, a))

# a = int(input())
# count = 0
# for i in range(1, a+1):
#     if a%i == 0:
#         print(f'{i}(은)는 {a}의 약수입니다.')
#         count += 1
# if count == 2:
#     print(f'{a}(은)는 1과 {a}로만 나눌 수 있습니다.')

# a = [88, 30, 61, 55, 95]
# count = 1
# for i in a:
#     if i >= 60:
#         print(f'{count}번 학생의 점수는 {i}점으로, 합격입니다.')
#     else:
#         print(f'{count}번 학생의 점수는 {i}점으로, 불합격입니다.')
#     count += 1

# str(1) # (1)
# int('30') # (2)
# int(5) # (3)
# bool('50') # (4)
# int('35') # (5)

# n = 5
# m = 9
# ga_ro = n * '*'
# for i in range(m):
# 	print(ga_ro)

# n = 5
# m = 9
# ga_ro = '*' * n + '\n'
# sagak_h = ga_ro * m
# print(sagak_h)

# print('''\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'''')

#근의공식

# a = int(input())
# b = int(input())
# c = int(input())

# ans1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
# ans2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# print(ans1, ans2)

# a = int(input())
# for i in range(1, a + 1):
# 	print(i)

# a = int(input())
# for i in range(a, -1, -1):
# 	print(i)

a = int(input())
ans = 0
for i in range(a + 1):
	ans = ans + i
print(ans)