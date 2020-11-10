
# 다음의 세 개의 라인은 Hello World 문자열을 화면에 출력한다.
# print("Hello Wolrd")
# print("Hello Wolrd")
# print('Hello Wolrd')
a = 10
b = 20

if a < b:
    # 들여쓰기 조심하기!!!
    # 새로운 자식블록이 생기면(조건문, 반복문, 함수정의)
    # 반드시 들여쓰기로 블록이 구분해야 한다.
    print(a)
    print('big')
    if a + 1 == 2:
        print(a + 1)
        print(a + 2)

print('end')
