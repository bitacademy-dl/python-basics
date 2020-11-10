# float형
# is_integer() 함수는 객체에 저장된 값이 정수인지 실수인지 판단한다.

a = 1.2
print(a, type(a))
print(a.is_integer())

b = 2.0
print(type(b))

c = 2.
print(type(c))
print(c.is_integer())

# 지수표현   0.0001 => 1e-4
# 다른 언어처럼 소수점 표현도 가능하고 e, E 지수표현도 가능하다.
d = 3e3
print(d)

e = 0.2e-4
print(e)