# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    rho = []
    for i in range(len(weights)):
        rho.append(values[i] / weights[i])
    for i in range(len(weights)):
        if capacity == 0:
            return value
        else:
            ind = rho.index(max(rho))
            value += min(weights[ind], capacity) / weights[ind] * values[ind]
            capacity -= min(weights[ind], capacity)
            del values[ind], weights[ind], rho[ind]
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

