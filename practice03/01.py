# 다음 세 개의 리스트가 있을 때,
# subs = [‘I’, ‘You’]
# verbs = [‘Play’, ‘Love’]
# objs = [‘Hockey’, ‘Football’]
# 3형식 문장을 모두 출력해 보세요


subjs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

for i in range(len(subjs)):
    for j in range(len(verbs)):
        for k in range(len(objs)):
            sentence = "%s %s %s." % (subjs[i], verbs[j], objs[k])
            print(sentence)