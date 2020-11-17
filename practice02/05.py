# 함수 sum를 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.


def sum(*arg):
    result = 0
    for n in arg:
        result += n

    return result


print(sum())
print(sum(1, 2))
print(sum(1, 2, 5, 7, 2, 3))


