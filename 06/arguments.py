print("======= 기본 인수값(default parameter) =========")


def incr(a, step=1):
    return a + step


a = incr(10)
print(a)

a = incr(10, step=5)
print(a)

a = incr(10, 10)
print(a)


# 문법오류
# def decr(step=1, a):
#    return a - step


print("======= 키워드 인수값(keyword parameter) =========")


def area(width, height):
    return width * height


print(area(10, 20))
print(area(width=10, height=20))
print(area(height=20, width=10))
print(area(10, height=20))
# print(area(20, width=10))
# print(area(height=20, 10))


print("======= 가변 인수값 =========")
def func2(*arg):
    print(arg)

func2(10, 20)
func2(10, 20, 30)
func2(10, 20, 30, 40)
# func2([10, 20])
# func2([10, 20, 30])
# func2([10, 20, 30, 40])

def func3(a, *arg):
    print(a, arg)
func3(10, 20)
func3(10, 20, 30)
func3(10, 20, 30, 40)


# 모든 인수를 sum
def sum2(*arg):
    s = 0
    for n in arg:
        s += n
    return s


print(sum2())
print(sum2(1, 2))
print(sum2(1, 2, 3, 4, 5))



