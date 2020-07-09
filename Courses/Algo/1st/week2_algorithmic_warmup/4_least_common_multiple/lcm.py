# Uses python3
import sys


def gcd_naive(a, b):
    if (a > b) and (b != 0):
        return gcd_naive(b, a % b)
    elif (a < b) and (b != 0):
        return gcd_naive(a, b % a)
    else:
        return a


def lcm_naive(a, b):
    return a * b // gcd_naive(a, b)


def main():
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


if __name__ == '__main__':
    main()

