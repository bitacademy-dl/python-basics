# if ~ else : 기거나아니거나
a = 10

if a > 5:
    print('big')
else:
    print('small')

# if ~ elif ~else
b = 10
if b > 0:
    print('양수')
elif b < 0:
    print('음수')
else:
    print('0')

# order = 'milk'
order = 'spagetti'
price = 0
# spam  price: 1000
# milk  price: 500
# egg  price: 100
if order == 'spam':
    price = 1000
elif order == 'milk':
    price = 500
elif order == 'egg':
    price = 100
else:
    price = '없는상품'

print(f'가격:{price}')




