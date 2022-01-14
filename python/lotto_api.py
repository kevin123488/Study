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
print(response)
# 당첨 번호 정보를 list에 담아보자
winners = []
# 1~7까지 반복
for num in range(1, 7):
    print(response[f'drwtNo{num}'])
    # winners 리스트에 당첨버호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)

# 997회차 요청 후 결과를 json을 통해 python으로 변경 후 출력

