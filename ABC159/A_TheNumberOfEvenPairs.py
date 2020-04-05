a, b = map(int, input().split())

ans = round((a * (a - 1) / 2) + (b * (b - 1) / 2))
print(ans)
