K, N = map(int, input().split())
A = list(map(int, input().split()))

distance = []

for i in range(N-1):
    dis = A[i + 1] - A[i]
    distance.append(dis)

dis = K - A[N - 1] + A[0]
distance.append(dis)

index = distance.index(max(distance))

print(K - distance[index])
