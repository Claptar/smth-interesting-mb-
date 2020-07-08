# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    fib_num = [0, 1]
    for i in range(1, n):
        fib_num.append((fib_num[i] + fib_num[i - 1]) % 10)
    return fib_num[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
