def Profile(matrix, k_mer):
    score = 1
    for i in range(len(k_mer)):
        score *= matrix[k_mer[i]][i]
    return score


def ProfileMostProbableKmer(text, k, profile):
    prob = 0
    k_best = ''
    for i in range(len(text) - k + 1):
        k_mer = text[i:i + k]
        if Profile(profile, k_mer) > prob:
            prob = Profile(profile, k_mer)
            k_best = k_mer
    return k_best