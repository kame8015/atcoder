A = [list(map(int, input().split())) for j in range(3)]

N = int(input())

B = [int(input()) for i in range(N)]

for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            A[i][j] = 0

for i in range(3):
    judge = 0
    for j in range(3):
        judge += A[i][j]
    if judge == 0:
        print("Yes")
        exit()

for j in range(3):
    judge = 0
    for i in range(3):
        judge += A[i][j]
    if judge == 0:
        print("Yes")
        exit()

judge = 0

for k in range(3):
    judge += A[k][k]
if judge == 0:
    print("Yes")
    exit()

judge = 0

judge += A[0][2] + A[1][1] + A[2][0]
if judge == 0:
    print("Yes")
else:
    print("No")
