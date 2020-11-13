# 문자열 데이터를 분석(학습)하기 전 처리함수 만들기
# 1. 공백제거
# 2. 필요 없는 문장 부호 빼기
# 3. 대소문자 정리(Capitalize 처리)
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina ', 'West virginia?']


def clean_strings(strings):
    results = []
    for string in strings:
        string = string.strip()                # 1
        string = re.sub('[!#?]', '', string)   # 2
        string = string.title()                # 3

        results.append(string)

    return results


states = clean_strings(states)
print(states)