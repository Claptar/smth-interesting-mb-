# Uses python3
import sys


def get_change(m):
    money = [10, 5, 1]
    count = 0
    for coin in money:
        num = m // coin
        if m == 0:
            return count
        elif num != 0:
            m -= num * coin
            count += num
    return count


if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = int(input())
    print(get_change(m))
