# for loop

print('=========== for loop 기본  ============')
a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')

print('=========== 복합 자료형의 for loop  ============')
l1 = [('둘리', 10), ('마이콜', 20), ('또치', 10)]
for t in l1:
    print('이름:%s, 나이:%d' % t)

for name, age in l1:
    print(f'이름:{name}, 나이:{age}')

print('=========== 1 ~ 10합 구하기  ============')
s = 0
for n in range(1, 11):
    # s = s + n
    s += n
print(s)

print('=========== break ============')
for i in range(10):
    if i > 5:
        break
    print(i, end=' ')
else:
    print('--end loop')

print('\n=========== continue ============')
for i in range(10):
    if i <= 5:
        continue
    print(i, end=' ')
else:
    print('--end loop')

print('=========== 삼각형1 ============')
for i in range(0, 5):
    print("*" * (i+1))

print('=========== 삼각형2 ============')
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end='')
    print('')

print('=========== 역삼각형1 ============')
print('=========== 역삼각형2 ============')

