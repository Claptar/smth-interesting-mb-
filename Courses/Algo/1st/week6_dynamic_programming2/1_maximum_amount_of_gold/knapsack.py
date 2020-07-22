# Uses python3
import sys


def optimal_weight(W, rocks):
    table = [[0] * (W + 1) for i in range(len(rocks) + 1)]
    rocks = [0] + rocks
    for i in range(1, len(rocks)):
        for w in range(1, W + 1):
            table[i][w] = table[i - 1][w]
            if w >= rocks[i] and table[i - 1][w - rocks[i]] + rocks[i] > table[i][w]:
                table[i][w] = table[i - 1][w - rocks[i]] + rocks[i]
    return table[len(rocks) - 1][W]


if __name__ == '__main__':
    W, n = map(int, input().split(' '))
    w = list(map(int, input().split(' ')))
    print(optimal_weight(W, w))
