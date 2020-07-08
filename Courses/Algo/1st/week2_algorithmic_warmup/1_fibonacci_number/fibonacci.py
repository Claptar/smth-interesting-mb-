# Uses python3
def calc_fib(n):
    fib_num = [0, 1]
    for i in range(1, n):
        fib_num.append(fib_num[i] + fib_num[i - 1])
    return fib_num[n]


n = int(input())
print(calc_fib(n))
