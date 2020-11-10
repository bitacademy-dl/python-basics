# 정수형

a = 23
b = 20 + 3

print(a, type(a))
print(b, isinstance(b, bool))
print(b, isinstance(b, int))

# 2진수, 10진수, 8진수, 16진수
c = 0b1101
print(c)

d = 0o23
print(d)

e = 0x23
print(d)

# python 3.x에서 int, long 합쳐졌다. 따라서 표현범위가 무한대다.
e = 2**1024
print(e, type(e))
print(e.bit_length())


# 변환함수
print(oct(38))
print(hex(38))
print(bin(38))








