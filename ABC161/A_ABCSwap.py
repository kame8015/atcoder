X = list(map(int, input().split()))

X[0], X[1] = X[1], X[0]
X[0], X[2] = X[2], X[0]

print(" ".join(map(str, X)))
