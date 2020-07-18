def HammingDistance(p, q):
    num = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            num += 1
    return num


def NumberToPattern(num, k):
    slovar = {0: "A", 1: "C", 2: "G", 3: "T"}
    pattern = ''
    while num > 3:
        pattern += slovar[num % 4]
        num = num // 4
        if num < 4:
            pattern += slovar[num]
    return 'A' * (k - len(pattern)) + pattern[::-1]

def Distance(Pattern, Dna):
    dist = 0
    for string in Dna:
        dist_s = len(string)
        for i in range(len(string) - len(Pattern) + 1):
            if HammingDistance(Pattern, string[i:i + len(Pattern)]) < dist_s:
                dist_s = HammingDistance(Pattern, string[i:i + len(Pattern)])
        dist += dist_s
    return dist


def MedianString(Dna, k):
    disnance = len(Dna[0])
    med = 'AAA'
    for i in range(4 ** k):
        patt = NumberToPattern(i, k)
        d = Distance(patt, Dna)
        if disnance > d:
            disnance = d
            med = patt
    return med
