results = []
for n in [1, 2, 3, 4, 5, 6]:
    results.append(n**2)
print(results)

results = [n**2 for n in [1, 2, 3, 4, 5, 6]]
print(results)

# 문자열 리스트에서 길이가 2 이하인 문자열 리스트 만들기
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
results = []
for s in strings:
    if len(s) <= 2:
        results.append(s)
print(results)

results = [s for s in strings if len(s) <= 2]
print(results)

# 369있는 수 리스트 만들기
results = []
for n in range(1, 1000):
    s = str(n)
    claps = s.count('3') + s.count('6') + s.count('9')
    if claps > 0:
        results.append(n)
print(results)

results = [n for n in range(1, 1000) if str(n).count('3') > 0 or str(n).count('6') > 0 or str(n).count('9') > 0]
print(results)


# set comprehension
# 문자열 리스트에서 길이가 2 이하인 문자열 set 만들기
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
results = {s for s in strings if len(s) <= 2}
print(results)

# dict comprehension
# 문자열 리스트에서 길이가 2 이하인 dict 문자:문자길이 만들기
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
results = {s: len(s) for s in strings if len(s) <= 2}
print(results)


