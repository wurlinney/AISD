import tracemalloc
import time

tracemalloc.start()

def exchanger(money, coins):
    MAX_VALUE = money + 1
    dp = [MAX_VALUE] * (money + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, money + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[money] if dp[money] != MAX_VALUE else -1





with open('input.txt', 'r') as file:
    money, k = map(int, file.readline().strip().split())
    coins = list(map(int, file.readline().strip().split()))

start_time = time.perf_counter()

result = exchanger(money, coins)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
