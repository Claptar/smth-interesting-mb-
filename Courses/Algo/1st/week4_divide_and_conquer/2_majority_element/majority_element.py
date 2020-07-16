# Uses python3
import sys


def pivot(a, l, r):
    k = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= k:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def q_sort(a, l, r):
    if l >= r:
        return
    m = pivot(a, l, r)
    q_sort(a, l, m - 1)
    q_sort(a, m + 1, r)


def get_majority_element(a):
    n = len(a)
    q_sort(a, 0, len(a) - 1)
    el = a[0]
    count = 0
    for i in range(n):
        if count > n / 2:
            return 1
        elif a[i] == el:
            count += 1
        else:
            el = a[i]
            count = 0
    if count >= n / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    n = input()
    a = list(map(int, input().split(' ')))
    print(get_majority_element(a))
