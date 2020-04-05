import collections

n = int(input())
a = list(map(int, input().split()))

count = collections.Counter(a)
sum = 0

# 全体の選び方をカウント
for x in count.values():
    sum += x * (x - 1) // 2

for k in a:
    print(sum - count[k] + 1)
