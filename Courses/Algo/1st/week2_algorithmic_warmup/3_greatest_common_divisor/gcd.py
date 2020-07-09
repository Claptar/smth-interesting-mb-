# Uses python3
import sys


def gcd_naive(a, b):
    if (a > b) and (b != 0):
        return gcd_naive(b, a % b)
    elif (a < b) and (b != 0):
        return gcd_naive(a, b % a)
    else:
        return a


def main():
    inp = sys.stdin.read()
    a, b = map(int, inp.split())
    #a, b = map(int, input().split())
    print(gcd_naive(a, b))


if __name__ == "__main__":
    main()
