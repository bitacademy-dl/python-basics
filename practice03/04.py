# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random

multiplys = {}

# 1.답이 다른 구구단 9문제 출제하기
while len(multiplys) != 9:
    lv = random.randrange(9) + 1
    rv = random.randrange(9) + 1
    multiplys[lv*rv] = (lv, rv)

# 2.제출 문제와 정답
correct_answer = random.choice(list(multiplys.keys()))
quest = multiplys[correct_answer]

# 3.문제 출력
print('%d X %d = ?' % quest, end='\n\n')

# 4.답들 출력
for i, k in enumerate(multiplys):
    print(k, end='\t')
    if (i+1) % 3 == 0:
        print()

# 5.답 입력받기
while True:
    answer = input('\nanswer: ')
    if answer.isdigit():
        answer = int(answer)
        break

# 6.결과출력
print('정답' if correct_answer == answer else '오답')