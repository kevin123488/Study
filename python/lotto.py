# 1~45중 6개만 뽑아서 리스트에 담아서 출력
# random 불러오기
import random
# requests 불러오기
import requests

# requests 사용해서 로또 api에 데이터 요청. get 요청-> 조회
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
response = requests.get(url).json()
# https:// + 고유주소 + ~~ + 
# ?뒤의 요소: 앞의 주소로 요청을 보낼건데
# 뒷부분: 요청보낼 값. 요청보낼 값은 &로 여러개 추가 가능.
# 위의 경우 method는 get, drwNo는 997
# 요청 보내서 응답 받은 문서 출력
# print(response)
# 당첨 번호 정보를 list에 담아보자
winners = []
# 1~7까지 반복
for num in range(1, 7):
    print(response[f'drwtNo{num}'])
    # winners 리스트에 당첨버호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)
# 1~45 불러오기
# range(a, b)일 경우, a~(b-1)까지 가져옴
# 리스트로 만들기
numbers = list(range(1, 46))

# 비복원추출로 6개 뽑기
# 6개 뽑아서 lotto 변수에 담기를 1000번 반복
for i in range(1000):
    lotto = random.sample(numbers, 6)
    # 당첨 횟수를 기록
    count = 0
    #print(lotto[0]~[5])
    for num in lotto:
        # print(num)
        # lotto가 가지고 있는 값들 하나하나가
        # winners 안에 들어있다면,
        if num in winners:
        # 한개 당첨    
            count = count + 1
        
        # 당첨 횟수를 기록. 사이클 한번당 횟수 초기화 필요
        # 숫자 6개를 다 확인하고 나서
        # 6개 당첨 == 1등
    if count == 6:
        print(i)
        print('1등!!!')