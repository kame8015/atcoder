N, A, B = map(int, input().split())

ans = 0

ans += A * (N // (A + B))

L = N % (A + B)
if L < A:
    ans += L
else:
    ans += A

print(ans)
