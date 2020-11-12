# enumerate

index = 1
for color in ['red', 'blue', 'yellow', 'gray']:
    print(f'{index}:{color}')
    index += 1


for i, color in enumerate(['red', 'blue', 'yellow', 'gray']):
    print(f'{i+1}:{color}')
