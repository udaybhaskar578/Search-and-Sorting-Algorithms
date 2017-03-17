import sys
n = raw_input().strip().split(' ')
n = list(map(int, n))
x=0
for i in n:
    x = x+i
print(x)

