# lambda

def blah(x):
    return x * 2


for i in range(10):
    print(f'{i}:{blah(i)}', end=' ')
else:
    print('')


# (x => x * 2)(i)
for i in range(10):
    print(f'{i}:{(lambda x: 2*x)(i)}', end=' ')
else:
    print('')
