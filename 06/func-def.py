# 함수 정의

print('=================함수 정의=====================')


def dummy():
    pass


def func1():
    print('Hello World')


def func2(name):
    print('Hello' + name)


def func3():
    return 'Hello World'


def times(a, b):
    return a * b


dummy()
func1()
func2('안대혁')
s = func3()
n = times(2, 2)
print(s, n)


print('=================여러 값을 반환할 수 있다=====================')


def func4():
    return 10, 20   # tuple auto packing을 통해 튜플 객체 하나를 반환한다.


a, b = func4()     # tuple auto unpacking을 통해 반환된 튜플 객체를 여러 변수에 대입할 수 있다.
print(a, b)


print('=================함수도 객체다.=====================')
print(func1)
print(type(func1))
f = func1
f()


