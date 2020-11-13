# object ID
import sys

i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))

i1 = 1234567890123456789
i2 = 1234567890123456789
print(hex(id(i1)), hex(id(i2)))

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

print(i1 is i2)
print(l1 is l2)
print(l1 == l2)
print(s1 is s2)

# ?
t1 = (1, 2, 3, 4, 5)
t2 = (1, 2, 3, 4, 5)
print(sys.getrefcount(t1))
print(t1 is t2)

t3 = t1
print(sys.getrefcount(t1))


