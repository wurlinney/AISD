import tracemalloc
import time

tracemalloc.start()

suits = 'SCDH'
ranks = '6789TJQKA'

def cards_matrix(player_cards):

    dp = [[False] * 4 for _ in range(9)]
    for card in player_cards:
        rank_idx = ranks.index(card[0])
        suit_idx = suits.index(card[1])
        dp[rank_idx][suit_idx] = True

    return dp


def can_defend(n, r, player_cards, enemy_cards):

    trump_suit_idx = suits.index(r)
    dp = cards_matrix(player_cards)
    for card in enemy_cards:
        enemy_rank, enemy_suit = ranks.index(card[0]), suits.index(card[1])
        card_covered = False

        for rank in range(enemy_rank + 1, 9):
            if dp[rank][enemy_suit]:
                dp[rank][enemy_suit] = False
                card_covered = True
                break

        if not card_covered and enemy_suit != trump_suit_idx:
            for rank in range(9):
                if dp[rank][trump_suit_idx]:
                    dp[rank][trump_suit_idx] = False
                    card_covered = True
                    break

        if not card_covered:
            return 'NO'

    return 'YES'


with open ('input.txt', 'r') as file:
    n, m, r = file.readline().strip().split()
    player_cards = list(file.readline().strip().split())
    enemy_cards = list(file.readline().strip().split())

start_time = time.perf_counter()

result = can_defend(n, r, player_cards, enemy_cards)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
