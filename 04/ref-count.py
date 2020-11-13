# 레퍼런스 카운트

import sys

x = object()
print(type(x))
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))

# 레퍼런스 값
del x
print(sys.getrefcount(y))

# x는 symbol table 에서 사라진다
# print(x)
