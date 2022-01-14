# import시 주의점
# import 가지고오는 행위
# 이 이후로 사용할 코드를 가지고 올 것이기 때문에
# import는 항상 최상단에 작성한다.

import random

menu = ['짜장면', '짬뽕', '탕수육']
#menu중 하나를 무작위로 선택
#함수를 쓸 땐 () 이용. f(x)
choice = random.choice(menu)

print(choice)