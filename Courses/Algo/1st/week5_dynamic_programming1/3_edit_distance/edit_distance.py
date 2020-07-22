import numpy as np


def edit_distance(s, t):
    s = ' ' + s
    t = ' ' + t
    D = [[len(s) + len(t)] * len(s) for i in range(len(t))]
    for j in range(len(s)):
        D[0][j] = j
    for i in range(len(t)):
        D[i][0] = i
    for i in range(1, len(t)):
        for j in range(1, len(s)):
            ins = D[i][j - 1] + 1
            dell = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mis_m = D[i - 1][j - 1] + 1
            if s[j] == t[i]:
                D[i][j] = min(ins, dell, match)
            else:
                D[i][j] = min(ins, dell, mis_m)
    return D[len(t) - 1][len(s) - 1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
