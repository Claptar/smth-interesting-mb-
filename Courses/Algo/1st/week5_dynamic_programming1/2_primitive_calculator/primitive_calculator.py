# Uses python3
import sys


def optimal_sequence(m):
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for num in range(2, m + 1):
        min_k_num = m
        last_num = m
        if a[num - 1] + 1 < min_k_num:
            min_k_num = a[num - 1] + 1
            last_num = num - 1
        if num % 2 == 0 and a[num // 2] + 1 < min_k_num:
            min_k_num = a[num // 2] + 1
            last_num = num // 2
        if num % 3 == 0 and a[num // 3] + 1 < min_k_num:
            min_k_num = a[num // 3] + 1
            last_num = num // 3
        a[num] = min_k_num
        b[num] = last_num
    c = []
    i = m
    while i > 0:
        c.append(i)
        i = b[i]
    return a[m], c[::-1]


n = int(input())
k, c = optimal_sequence(n)
print(k)
for x in c:
    print(x, end=' ')
