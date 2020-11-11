print('============== 생성 ================')
l1 = []
l2 = [1, True, 'python', 3.14]

print('============== 인덱싱 ================')
print(l2[0], l2[1], l2[2], l2[3])
print(l2[-4], l2[-3], l2[-2], l2[-1])

print('============== 반복 ================')
l3 = l2 * 2
print(l3)

print('============== 연결 ================')
l4 = l2 + [1, 2, 3]
print(l4)

print('============== 길이 ================')
print(len(l4))

print('=========== in, not in ============')
print(5 in l4)
print(5 not in l4)

print('=========== slicing ============')
l5 = [0, 1, 2, 3, 4, 5]
print(l5[1:4])
print(l5[0:6])
print(l5[:])
print(l5[2:])
print(l5[5::-1])
print(l5[-1::-1])

print('=========== 변경가능한 객체(mutable) ============')
del l5[2]
print(l5)
l5[1] = l5[1] + 1
print(l5)

print('=========== 치환: slicing ============')
a = [1, 12, 123, 1234]
a[0:2] = [10, 20]
print(a)

a[0:2] = [100]
print(a)

a[1:2] = [200]
print(a)

a[2:3] = [300, 400, 500]
print(a)

print('=========== 삭제: slicing ============')
a = [1, 12, 123, 1234]
a[1:2] = []
print(a)

a[0:] = []
print(a)

print('=========== 삽입: slicing ============')
a = [1, 12, 123, 1234]

# 중간 삽입
a[1:1] = ['a']
print(a)

# 마지막 삽입
a[5:] = [12345]
print(a)

# 처음 삽입
a[:0] = [0]
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)

print('=========== 객체함수: 삽입 ============')
a = [1, 3, 4]

# 중간
a.insert(1, 2)
print(a)

# 뒤에
a.append(5)
print(a)

# 앞에
a.insert(0, 0)
print(a)

print('=========== 객체함수: reverse ============')
a.reverse()
print(a)

print('=========== 객체함수: 삭제 ============')
# 값으로 삭제
a.remove(3)
print(a)
try:
    a.remove(3)
except ValueError as e:
    print('값이 없는 경우 삭제시 예외 발생')

print('=========== 객체함수: 스택(Stack)으로 사용하기 ============')
stck = []
stck.append(10)  # push
stck.append(20)  # push
stck.append(30)  # push

print(stck)

print(stck.pop())  #pop
print(stck.pop())  #pop

print(stck)

print('=========== 객체함수: 큐(Queue)로 사용하기 ============')
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print(q)











