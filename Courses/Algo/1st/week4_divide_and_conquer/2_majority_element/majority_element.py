# Uses python3
import sys


def pivot(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
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
    dic = {}
    n = len(a) / 2
    for s in a:
        if s in dic:
            dic[s] += 1
            if dic[s] > n:
                return 1
        else:
            dic[s] = 1
    return 0



if __name__ == '__main__':
    n = input()
    a = list(map(int, input().split(' ')))
    print(get_majority_element(a))
