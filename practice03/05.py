# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.

nums = [5, 9, 3, 8, 60, 20, 1]

print('Before Sort.')
for num in nums:
    print(num, end=' ')
else:
    print()

count = len(nums)
for i in range(count):
    for j in range(count-1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("After Sort.")
for num in nums:
    print(num, end=' ')
else:
    print()