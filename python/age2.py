import requests

name = input('이름을 입력해 주십시오: ')
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()
age = response['age']
print(f'{name}의 나이는 {age}살 입니다.')