# global, local 심벌 테이블
g_a = 1
g_s = '둘리'


def g_f():
    l_a = 2
    l_s = '마이콜'
    print(locals())


print("=========== Global Symbol Table vs Local Symbol Table ================")
print(globals())
g_f()

print(g_a)
# 에러: local symbol table은 함수가 실행이 끝나면 사라진다.
# print(l_a)


print("=========== 01. 사용자 정의 함수 ================")
# 심벌테이블 O, 확장 O
g_f.n = 'hello'
g_f.i = 10
print(g_f.__dict__)

print("=========== 02. 사용자 정의 클래스 ================")
# 심벌테이블 O, 확장 O
class MyClass:
    x = 10
    y = 20

MyClass.z = 30
print(MyClass.__dict__)

print("=========== 03. 내장함수 ================")
# 심벌테이블 x, 확장 x
# print.z = 10
# print(print.__dict__)


print("=========== 04. 내장클래스 ================")
# 심벌테이블 o, 확장 x
# str.z = 10
print(str.__dict__)


print("=========== 05. 사용자 정의 클래스로 생성된 객체 ================")
# 심벌테이블 o, 확장 o
o = MyClass()
o.z = 10
print(o.__dict__)


print("=========== 06. 내장 클래스로 생성된 객체 ================")
# 심벌테이블 x, 확장 x
# g_a.z = 10
# print(g_a.__dict__)
