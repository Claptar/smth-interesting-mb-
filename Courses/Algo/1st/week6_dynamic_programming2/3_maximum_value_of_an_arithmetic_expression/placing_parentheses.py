# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maxmin(num, op, M, m, i , j):
    mini =  max(num) ** (len(num) // 2)
    maxi = - max(num) ** (len(num) // 2)
    for k in range(i, j):
        eq1 = evalt(M[i][k], M[k + 1][j], op[k])
        eq2 = evalt(M[i][k], m[k + 1][j], op[k])
        eq3 = evalt(m[i][k], M[k + 1][j], op[k])
        eq4 = evalt(m[i][k], m[k + 1][j], op[k])
        mini = min(mini, eq1, eq2, eq3, eq4)
        maxi = max(maxi, eq1, eq2, eq3, eq4)
    return mini, maxi


def get_maximum_value(num, op):
    n = len(num)
    M = [[0] * n for i in range(n)]
    m = [[0] * n for i in range(n)]
    for i in range(n):
        M[i][i] = num[i]
        m[i][i] = num[i]
    for i in range(1, n):
        for j in range(n - i):
            m[j][i + j], M[j][i + j] = maxmin(num, op, M, m, j, i + j)
    return M[0][len(num) - 1]


def dataset_conv(dataset):
    num = []
    op = []
    for el in dataset:
        if el.isdigit():
            num.append(int(el))
        else:
            op.append(el)
    return num, op


if __name__ == "__main__":
    dataset = input()
    num, op = dataset_conv(dataset)
    print(get_maximum_value(num, op))
