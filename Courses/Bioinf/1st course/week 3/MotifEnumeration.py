def ApproximatePatternCount(Text, Pattern, d):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Text[i:i + len(Pattern)], Pattern) <= d:
            count += 1
    return count


def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    Neighborhood = set()
    suff = Pattern[1:]
    SuffixNeighbors = Neighbors(suff, d)
    for neib in SuffixNeighbors:
        if HammingDistance(neib, suff) < d:
            for x in ['A', 'C', 'G', 'T']:
                Neighborhood.add(x + neib)
        else:
            Neighborhood.add(Pattern[0] + neib)
    return list(Neighborhood)


def HammingDistance(p, q):
    num = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            num += 1
    return num


def MotifEnumeration(dna, k, d):
    Patterns = set()
    string = ''.join(dna)
    for i in range(len(string) - k + 1):
        for pat in Neighbors(string[i:i + k], d):
            if all(ApproximatePatternCount(x, pat, d) for x in dna):
                Patterns.add(pat)
    return list(Patterns)



k = 3
d = 1
dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
print(MotifEnumeration(dna, k, d))

