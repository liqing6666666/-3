import time

N = int(input())
lst1 = list(map(int, input().split()))  # map函数,对列表元素化为整型，返回一个map对象
start = time.perf_counter()
sum2 = 0  # 记录最大值
t = N
mx = 0
for i in range(N):
    mx += i
for i in range(N):
    m, n, j, sum1, t = 1, 0, i, 0, N
    lst2 = lst1[:]
    # 分别赋值的过程,m为数的数字,n记录赢得的卡片张数,lst[j]为当前开始的卡片号，sum1为此次赢得的球票之和,t为剩余的卡片数
    while m <= N and n < N:
        if j >= t: j = 0
        if m == lst2[j]:
            sum1 += lst2[j]
            del lst2[j]  # 删除卡片lst2[j]
            t -= 1  # 剩余的卡片数减一
            m = 1  # 重新开始数
            n += 1  # 赢得的卡片数加一
            continue
        m += 1
        j += 1
    if sum1 > sum2: sum2 = sum1  # 取最大值
    if sum2 == mx: break
print(sum2)
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")
