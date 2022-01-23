# def list_sum(args):
#     sum = 0
#     for i in range(len(args)):
#         sum += args[i]
#     return sum

# def all_list_sum(args):
#     sum = 0
#     for i in args:
#         for k in i:
#             sum += k
#     return sum

# result = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
# print(result)

# 딕셔너리로 이루어진 list의 합 구하기
# def dict_list_sum(args):
#     sum = 0
#     for i in args:
#         sum += i['age']
#     return sum

# result = dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])
# print(result)

# 2차원 list의 전체 합 구하기
# def all_list_sum(args):
#     sum = 0
#     for i in args:
#         for k in i:
#             sum += k
#     return sum

# result = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
# print(result)

# workshop 4
# 1. 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하라
# def get_secret_word(args):
#     strr_ing = ''
#     for i in args:
#         strr_ing += chr(i)
#     return strr_ing

# result = get_secret_word([83, 115, 65, 102, 89])
# print(result)

# 2. 문자열을 전달 받아 해당 문자열과 대응하는 아스키 숫자들의 합을 반환하라
# def get_secret_number(args):
#     sum = 0
#     for i in args:
#         sum += ord(i)
#     return sum

# result = get_secret_number('tom')
# print(result)

# 3. 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여
# 더 큰 합을 가진 문자열을 반환하라
# def get_strong_word(args1, args2):
#     sum1 = 0
#     sum2 = 0
#     for i in args1:
#         sum1 += ord(i)
#     for k in args2:
#         sum2 += ord(k)
    
#     if sum1 > sum2:
#         return args1
#     elif sum1 == sum2:
#         return '값이 동일하므로 어느 한 값을 출력할 수 없습니다'
#     else:
#         return args2

# result1 = get_strong_word('z', 'a')
# result2 = get_strong_word('tom', 'john')
# print(result1, result2)