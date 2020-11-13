# 인수값 전달 방법
# call by reference******
# call by value


def f(i):
    i = 20


def f2(seq):
    seq[0] = 10


a = 10
print(a)
f(a)
print(a)


# 컨테이너형 불변 객체를 파라미터로 사용하고
# 내부에서 변경하는 경우 (오류)
# t = (1, 20, 30, 40)
# f2(t)

# 컨테이너형 가변 객체를 파라미터로 사용하는 경우
# 내부에서 변경하는 경우
l = [1, 20, 30, 40]
f2(l)
print(l)
