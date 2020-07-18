# Uses python3
import sys


def get_change(m):
    coins = [1, 3, 4]
    a = [0] * (m + 1)
    for summa in range(1, m + 1):
        min_coin_num = m
        for coin in coins:
            last_coin = summa - coin
            if last_coin >= 0 and a[last_coin] + 1 < min_coin_num:
                min_coin_num = a[summa - coin] + 1
        a[summa] = min_coin_num
    return a[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
