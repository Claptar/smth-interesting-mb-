def Profile(matrix, k_mer):
    score = 1
    for i in range(len(k_mer)):
        score *= matrix[k_mer[i]][i]
    return score


def ProfileMostProbableKmer(text, k, profile):
    prob = 0
    k_best = text[:k]
    for i in range(len(text) - k + 1):
        k_mer = text[i:i + k]
        if Profile(profile, k_mer) > prob:
            prob = Profile(profile, k_mer)
            k_best = k_mer
    return k_best


def profile_matrix(motifes_matrix):
    n = len(motifes_matrix[0])
    profile = {x:[0] * n for x in ['A', 'C', 'G', 'T']}
    for i in range(n):
        for motif in motifes_matrix:
            profile[motif[i]][i] += 1 / n
    return profile


def Score(motifs):
    score = 0
    profile = profile_matrix(motifs)
    for i in range(len(profile['A'])):
        score += 1 - max([profile[x][i] for x in ['A', 'C', 'G', 'T']])
    return score


def GreedyMotifSearch(Dna, k, t):
    best_motifs = [string[:k] for string in Dna]
    for i in range(len(Dna[0]) - k + 1):
        motifs = []
        motifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            profile = profile_matrix(motifs)
            motifs.append(ProfileMostProbableKmer(Dna[j], k, profile))
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
    return best_motifs
