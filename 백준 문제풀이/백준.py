# 정수 N개의 합.
# 정수 N개가 주어졌을 때, N개의 합을 구하는 함수를 작성하시오

# def solve(*a):
#     ans = 0
#     for i in a:
#         ans += i
#     return ans
# result = solve(1, 2, 3, 4, 5)
# print(result)
# *a의 형태로 파라미터를 두면 변수로 여러개의 숫자를 넣을 수 있음
# 여러 숫자를 위의 형식과 같이 넣어주면, a에 tuple 형식으로 값이 저장됨
# tuple은 순회 가능한 요소이므로 for문 써서 하나씩 더하기 ㄱ

# ---------------------------------------------

# 셀프 넘버
# 함수 d(n)을 n과 n의 각 자리수를 더하는 함수라고 하자.
# 이 때, 결과값 d(n)에 대해 n을 d(n)의 생성자라고 한다.
# 생성자가 없는 수를 '셀프 넘버'라고 한다.
# 10000 이하의 '셀프 넘버'를 모두 출력하는 코드를 작성하라.

# 1. 자리수를 더하는 함수 작성
# def d(n):
#     plus_jarisoo = 0
#     for i in range(len(str(n))):
#         plus_jarisoo += (n//10**i) % 10
#     return plus_jarisoo + n

# # 1부터 10000까지의 d(n)값을 리스트에 넣고
# # 1~10000의 숫자 중 리스트에 없는 값을 고르면?

# lis_t = []
# for i in range(1, 10001):
#     lis_t += [d(i)]

# for k in range(1, 10001):
#     if k in lis_t:
#         pass
#     else:
#         print(k)

# --------------------------------------------

# 한수
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룰 경우, 그 수를 한수라고 한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하라.

# 내 풀이
# N = int(input())

# def han_soo(args):
#     # 받는 정수를 문자열로 변환
#     A = str(args)
#     # '정수' 형태를 순회
#     lis_t = []
#     for i in A:
#         # 1234라는 수를 넣었다 치면, A = '1234'
#         # i에 '1', '2', '3', '4'가 차례로 들어감
#         lis_t += [int(i)] # lis_t = [1, 2, 3, 4]
    
#     for k in lis_t:
#         deun_cha = 0
#         deun_cha -= k
#         for j in lis_t:
#             deun_cha += j+1
#             if deun_cha/(len(lis_t)-1):
#                 return True
#             else:
#                 return False

# for hans in range(1, N+1):
#     lllist = []
#     if han_soo(hans) == True:
#         lllist += [hans]
# print(len(lllist))
# 결과 -> 에러

# 문제 다시 읽고 풀어본다
# 1000 이하의 수 이므로, 자릿수에 맞춰 고려 ㄱ
# 1, 2자리의 숫자의 경우 무적권 한수.
# 4자리의 숫자의 경우 한수 아님. 1000밖에 없는데, 1000은 한수가 아니기 때문임.
# 그럼 남은건 3자리 숫자 뿐이네

# N = int(input())

# def han_soo_pandokgi(args):
#     if 99 < args < 1000:
#         lis_t = []
#         for i in str(args):
#             lis_t += [int(i)]
#         if lis_t[0] - lis_t[1] == lis_t[1] - lis_t[2]:
#             return True
#         else:
#             return False
#     elif args == 1000:
#         return False
#     elif 0 < args < 100:
#         return True
#     else:
#         return False


# count = 0

# for i in range(1, N+1):
#     if han_soo_pandokgi(i):
#         count += 1
# print(count)