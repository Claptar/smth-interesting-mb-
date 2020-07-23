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


def get_maximum_value(num, op):
    n = len(num)
    M = [[0] * n for i in range(n)]
    m = [[0] * n for i in range(n)]
    for i in range(n):
        M[i][i] = num[i]
        m[i][i] = num[i]
    for i in range(1, n):
        for j in range(n - i):
            eq1 = evalt(M[j][i + j - 1], M[j + 1][i + j], op[i - 1 +j])
            eq2 = evalt(m[j][i + j - 1], M[j + 1][i + j], op[i - 1 +j])
            eq3 = evalt(M[j][i + j - 1], m[j + 1][i + j], op[i - 1 +j])
            eq4 = evalt(m[j][i + j - 1], m[j + 1][i + j], op[i - 1 +j])
            M[j][i + j] = max(eq1, eq2, eq3, eq4)
            m[j][i + j] = min(eq1, eq2, eq3, eq4)
    return M, m


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
    dataset = '5-8+7*4-8+9'
    num, op = dataset_conv(dataset)
    print(get_maximum_value(num, op))
