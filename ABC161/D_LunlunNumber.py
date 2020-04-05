import queue

K = int(input())

count = 0
q = queue.Queue()
for i in range(1, 10):
    count += 1
    q.put(i)
    if count == K:
        print(i)
        break

result = 0
while count != K:
    tmp = q.get()  # 先頭のキューを取り出す
    keta1 = tmp % 10  # 1の位を取得
    for i in range(-1, 2):
        if keta1 == 0 and i == -1:  # 1の位が0のとき
            continue
        if keta1 == 9 and i == 1:  # 1の位が9のとき
            continue
        result = tmp * 10 + (keta1 + i)
        q.put(result)  # 最後に付け足す
        count += 1
        if count == K:
            print(result)
            break
        else:
            continue
