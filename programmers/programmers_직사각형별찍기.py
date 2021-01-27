a, b = map(int, input().split())
for i in range(b):
    print('*' * a)

#다른사람 풀이
a, b = map(int, input().split())
print(('*' * a + '\n') * b)
