## Break, Continue, Pass에 대해

1. Break

-> 반복문을 멈추고 loop 밖으로 나가게 한다.

```python
# ex
for i in range(10):
    if i % 2 == 0:
        break
        print(i)
    else:
        print(i)
print("Done")

#실행화면
Done
```

이유는?

for i in range(10): 에 의해 i에 0부터 9까지의 수를 하나씩 대입하여 아래의 if문에 적용.

if i % 2 == 0: 에서 i에 0을 대입하면 해당 if문은 참이 됨.

if문이 참일 경우 **break 실행, 해당 for문 종료**하고 print("Done")로 이동함.



2. continue

-> 바로 다음 순번의 loop를 수행한다.

```python
# ex
for i in range(10):
    if i % 2 == 0:
        continue
        print(i)
    print(i)
print("Done")

#실행화면
1
3
5
7
9
Done
```

이유는?

for i in range(10): 에 의해 i에 0부터 9까지의 수를 하나씩 대입하여 아래의 if문에 적용.

if i % 2 == 0: 에서 i에 0을 대입하면 해당 if문은 참이 됨.

if문이 참일 경우 **continue 실행, 해당 loop는 넘기고 다음 loop(i = 1의 루프) 시작.**





3. pass

-> 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행. 그냥 빈자리 채워넣기라고 생각 ㄱ