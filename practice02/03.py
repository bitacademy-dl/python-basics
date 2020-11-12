# 다음 문자열을 모든 대문자를 소문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 각 단어를 순서대로 출력하세요.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

words = ['we', 'everyone', 'python']
words.sort(key=str)
print(words)

