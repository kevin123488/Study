import random
winners = [1, 2, 3, 4, 5, 6, 7]
numbers = list(range(1, 10))

for i in range(10):
    lotto = random.sample(numbers, 7)
    count = 0
    for num in lotto:
        if num in winners:
            count = count + 1
    if count == 6:
        print('성공')
    else:
        print('ㅋ')