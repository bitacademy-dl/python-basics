# 숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는
# 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게",
# 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

import random

while True:
    mi, ma, trycount = 1, 100, 1
    n = random.randrange(ma) + mi
    print('수를 결정하였습니다. 맞추어 보세요')

    while True:
        print('{0}-{1}'.format(mi, ma))
        gn = int(input('{0}>>'.format(trycount)))

        if gn == n:
            print('맞았습니다')
            break

        if gn < n:
            print('더 높게')
            mi = gn
        else:
            print('더 낮게')
            ma = gn

        trycount += 1

    if 'y' != input('다시 하시겠습니까(y/n)>>'):
        break
