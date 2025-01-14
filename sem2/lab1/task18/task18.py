import tracemalloc
import time

tracemalloc.start()

def find_min_cost(n, costs):
    costs = [0] + costs
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(0, n):
            if costs[i] <= 100:
                dp[i][j] = min(dp[i-1][j] + costs[i], dp[i-1][j+1])
            else:
                dp[i][j] = min(dp[i-1][j-1] + costs[i], dp[i-1][j+1])
    min_cost = min(dp[n])
    unused_cupons = dp[n].index(min_cost)

    cur_min = min_cost
    days = []
    for i in range(n, 0, -1):
        if cur_min in dp[i-1]:
            days.append(i)
        else:
            cur_min -= costs[i]

    used_cupons = len(days)

    return min_cost, unused_cupons, used_cupons, days[::-1]


with open ('input.txt', 'r') as file:
    n = int(file.readline())
    costs = list(map(int, file.readlines()))

start_time = time.perf_counter()

min_cost, unused_coupons, used_coupons, day_coupon = find_min_cost(n, costs)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(min_cost) + '\n')
    file.write(f"{unused_coupons} {used_coupons}\n")
    file.write(" ".join(map(str, day_coupon)) + "\n")

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")