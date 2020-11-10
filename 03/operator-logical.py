# 논리연산자 (not, or, and)

a = 30
b1 = a <= 30

# not
# not True -> False
# not False -> True
b2 = not b1

# or(논리합)
# False or False -> False
# True or False -> True
# False or True -> True
# True or True -> True
b3 = (a <= 30) or (a >= 100)

# and(논리곱)
# False and False -> False
# True and False -> False
# False or True -> False
# True or True -> True
b4 = (a <= 30) and (a >= 100)
# b4 = 100 <= a <= 30

print(b1, b2, b3, b4)

# 논리식의 계산순서
print(True or 'logical')
print(False or 'logical')
print([] or 'logical')
print([10, 20] or 'logical')
print('operator' or 'logical')
print('' or 'logical')
print('' or 'logical')
print(None or 'logical')


s = 'hello world'
# if s is not '':
#     print(s)
s and print(s)

s = ''
s and print(s)

print('--------------')




