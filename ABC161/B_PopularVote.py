N, M = map(int, input().split())
A = list(map(int, input().split()))

judge = sum(A) / (4 * M)

ans = 0
for i in range(N):
    if A[i] >= judge:
        ans += 1

if ans >= M:
    print("Yes")
else:
    print("No")
