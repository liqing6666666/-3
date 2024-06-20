import time

N = int(input())
lst = list(map(int, input().split()))  # map函数,对列表元素化为整型，返回一个map对象

start = time.perf_counter()
sum2 = 0  # 记录最大值
mx = 0
for i in range(1, N+1):
    mx += i
for i in range(N):
    m, n, j, sum1 = 1, 0, i, 0
    print(j)
    # 分别赋值的过程,m为数的数字,n记录赢得的卡片张数,lst[j]为当前开始的卡片号，sum1为此次赢得的球票之和
    visited = [0] * N  # 得到一个长度为N的元素都为0的列表来记录卡牌的状态,赢走了为1，没赢走为0
    while m <= N and n < N:  # m超过卡片数量就不会再相等了或全部赢完了
        if j == N: j = 0  # j=N时自动转为0
        print(lst[j], end=' ')

        if visited[j] == 1:
            j += 1
            continue

        if m == lst[j] and visited[j] == 0:  # 相等且没有被赢走
            sum1 += lst[j]  # 将球票数加起来
            visited[j] = 1  # 状态为1
            m = 1  # 找到后重新开始数
            n += 1  # 赢得的卡片数加一
            j += 1
            continue
        if visited[j] == 0: m += 1  # 状态为0时才数，状态为1不数跳过
        j += 1

    if sum1 > sum2: sum2 = sum1
    print()
    if sum2 == mx: break


print(sum2)
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")
