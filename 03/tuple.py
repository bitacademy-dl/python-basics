print('=========== 생성 ============')
t1 = ()         # 공튜플
t2 = (1, )      # 항목이 하나인 튜플을 생성할 때는 반드시 코마를 사용한다.

t3 = (1, 2, 3)
print(t3, type(t3))

print('=========== 인덱싱 ============')
print(t3[-3], t3[-2],t3[-1], t3[0], t3[1], t3[2])

print('=========== slicing ============')
print(t3[1:3])
print(t3[:])
print(t3[::-1])

print('=========== 반복 ============')
t4 = t3 * 2
print(t4)

print('=========== 연결 ============')
t5 = t3 + (4, 5, 6)
print(t5)

print('=========== 길이 ============')
print(len(t5))

print('=========== not, not in 연산 ============')
print(5 in t5)

print('=========== immutable ============')
# t6 = ('apple', 'banana', 10, 20)
# t6[2] = 90

print('=========== 여러값 대입 ============')
x, y, z = 10, 20, 30
print(x, y, z)

print('=========== 여러값 치환 ============')
x, y = 10, 20
print(x, y)
y, x = x, y
print(x, y)

print('=========== 객체함수 ============')
t = (20, 30, 40, 50, 20)
print(t.index(30))
print(t.count(20))

# 변환1
s = set(t)
print(s, type(s))

# 변환2(tuple -> list, list -> tuple)
l1 = list(t)
print(l1, type(l1))
t2 = tuple(l1)
print(t2, type(t2))

