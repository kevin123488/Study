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

# a = int(input())
# ans = 0
# for i in range(a + 1):
# 	ans = ans + i
# print(ans)

# a = range(1, 51)
# l_ist = []
# for i in a:
# 	if i % 2 == 1:
# 		l_ist.append(i)
# 	else:
# 		continue
# print(l_ist)

# n = 5
# m = 9
# ga_ro = '*' * n
# for i in range(m):
# 	print(ga_ro)

# scores = [80, 89, 99, 83]
# ans = 0
# for i in scores:
# 	ans = ans + i

# ave = ans / len(scores)
# print(ave)

# N = int(input())
# for i in range(1, N + 1):
# 	if N%i == 0:
# 		print(i)
# 	else:
# 		continue

# numbers = [
# 	85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 
# 	51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 
# 	52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
# ]
# numbers.sort()

# a = len(numbers)

# if a%2 == 0:
# 	print('중간값 없음')
# else:
# 	print(numbers[a//2])

# a = int(input())
# for i in range(1, a+1):
# 	for k in range(1, i+1):
# 		print(k, end='')
# 	print()

# numbers = [
# 	85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 
# 	51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 
# 	52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
# ]
# numbers.sort()

# a = len(numbers)

# if a%2 == 0:
# 	print('중간값 없음')
# else:
# 	print(numbers[a//2])

# a = int(input())
# for i in range(1, a+1):
# 	for k in range(1, i+1):
# 		print(k, end=' ')
# 	print()

#득표수 구하기, practice 1.2 문제
# students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
# count = 0
# for i in students:
# 	if i == '이영희':
# 		count += 1
# print(count)

#최댓값 구하기, practice 1.3 문제
# numbers = [7, 10, 22, 4, 3, 17]
# numbers.sort()
# print(numbers[-1])

#최솟값 구하기, practice 1.4 문제
# numbers = [7, 10, 22, 4, 3, 17]
# numbers.sort()
# print(numbers[0])

#최댓값과 등장 횟수 구하기, practice 1.5 문제
# numbers = [7, 10, 22, 7, 22, 22]
# numbers.sort()
# a = numbers[-1]
# count = 0
# for i in numbers:
# 	if i == a:
# 		count += 1
# print(a, count)

#5의 개수 구하기, practice 1.6 문제
# numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
# count = 0
# for i in numbers:
# 	if i == 5:
# 		count += 1
# print(count)

#'a'가 싫어, practice 1.7 문제
# word = input()
# output = ''
# for i in range(len(word)):
# 	wo_rd = word[i]
# 	if wo_rd != 'a':
# 		output += wo_rd
# print(output)

#단어 뒤집기, practice 1.8 문제
# word = input()
# word_length = len(word)
# output = ""
# for i in range(word_length):
# 	char = word[word_length-1-i]
# 	output += char
# print(output)

#단어 뒤집기 다시 해보기
# word = input()
# reverse_word = ''
# for i in range(len(word)):
# 	re_v = word[len(word) -1 -i]
# 	reverse_word += re_v
# print(reverse_word)

# word = input()
# result = ''
# for char in word:
#     if char != 'a':
#         result += char
# print(result)

# word = input()
# result = ''
# for char in word:
#     if char == 'a':
#         continue #char이 'a'이면 그냥 넘겨버려
#     else:
#         result += char #char이 'a'가 아닌 상황이니, char을 result에 더한 후 대입ㄱ
# print(result)

# n까지의 총합
# 1. for문 사용
# num = int(input())
# su_m = 0
# for i in range(1, num+1):
#     su_m += i
# print(su_m)

# 2. while문 사용
# num = int(input())
# su_m = 0
# i = 0
# while i <= num:
#     su_m += i
#     i = i + 1
# print(su_m)

# 리스트의 총 곱
# 1. for문 사용
# num = int(input())
# gophagi = 1
# for i in range(1, num + 1):
#     gophagi = gophagi * i
# print(gophagi)

# 2. while문 사용
# num = int(input())
# gophagi = 1
# i = 1
# while i <= num:
#     gophagi = gophagi * i
#     i += 1
# print(gophagi)