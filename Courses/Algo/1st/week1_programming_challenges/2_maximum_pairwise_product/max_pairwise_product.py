def max_pairwise_product(numbers):
    numbers.sort()
    return numbers[len(numbers) - 1] * numbers[len(numbers) - 2]


def max_pairwise_product2(num):
    maxi1 = 0
    for i in range(1, len(num)):
        if num[i] > num[maxi1]:
            maxi1 = i
    maxi2 = 0
    for i in range(0, len(num)):
        if num[i] > num[maxi2] and num[i] != num[maxi1]:
            maxi2 = i
    return num[maxi1] * num[maxi2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product2(input_numbers))
