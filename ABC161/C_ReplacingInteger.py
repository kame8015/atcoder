N, K = map(int, input().split())

N = N % K

if N >= abs(N - K):
    N = abs(N - K)

print(N)
