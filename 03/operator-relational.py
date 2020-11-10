# 객체의 대소 비교
print(1 > 3)
print(2 < 4)
print(1 >= 3)
print(1 <= 4)
print(1 == 3)
print(1 != 3)

# 복합관계식 지원
# 0 < a < 10
a = 4
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 다른 타입 객체 비교
print('abcde' > 'abc')
print('aac' > 'abc')
print([1, 2, 3] < [1, 2, 4])
print((1, 2, 3) < (1, 2, 4))

# 동질성   ==
# 동일성   is
a = 20
b = 20
c = a
print(a == b)  # True
print(a is b)  # True
print(a is c)  # True
print(a == c)  # True




