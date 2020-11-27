# test for Add
try:
    from add import Add
    from multiply import Multiply
except ImportError as e:
    print(e)

a = Add()
out = a.forward(10, 20)
print(out)
print(a)

# test for Multiply
m = Multiply()
out = m.forward(10, 20)
print(out)   # 200
print(m)     # 'Multiply(x=10, y=20)'
