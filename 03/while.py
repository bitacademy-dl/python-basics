# while loop

print('=========== while loop 기본  ============')
count = 1
while count < 11:
    print(count, end=' ')
    count += 1
else:
    print('')

print('=========== 1 ~ 10합  ============')
s, n = 0, 1
while n <= 10:
    s += n
    n += 1
print(s)

print('=========== break ============')
i = 0
while i < 10:
    if i > 5:
        break
    print(i, end=' ')
    i += 1
else:
    print('---- end loop')

print('\n=========== continue ============')
i = 0
while i < 10:
    i += 1

    if i <= 5:
        continue
    print(i, end=' ')
else:
    print('---- end loop')

print('=========== infinite loop(무한루프) ============')
i = 0
while True:
    print(i, end=' ')
    if i > 5:
        break
    i += 1
else:
    print('else block')
