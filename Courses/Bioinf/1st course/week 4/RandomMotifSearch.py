import random


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


def random_motif_genetator(dna, k):
    motifs = []
    for string in dna:
        i = random.randint(0, len(string) - k)
        motifs.append(string[i:i + k])
    return motifs


def Profile_score(matrix, k_mer):
    """
    Using profile-matrix finds out score of k-mer
                    A: 1/2 1/2 0 1/2
    matrix          C: 1/4 1/4 0  0      k-mer: ACTG  
    example:        G: 1/4  0  0 1/4
                    T:  0  1/4 1 1/4
    Output: 0.5 * 0.25 * 1 * 0.25 = 1/32
    """
    score = 1
    for i in range(len(k_mer)):
        score *= matrix[k_mer[i]][i]
    return score


def ProfileMostProbableKmer(text, k, profile):
    """
    Searching for the most probable k-mer in text
    using profile-matrix
    """
    prob = 0
    k_best = text[:k]
    for i in range(len(text) - k + 1):
        k_mer = text[i:i + k]
        if Profile_score(profile, k_mer) > prob:
            prob = Profile_score(profile, k_mer)
            k_best = k_mer
    return k_best


def motifs_from_profile(dna, k, profile):
    """
    Using profile-matrix finding the most probable k-mer in each string
    """
    return [ProfileMostProbableKmer(string, k, profile) for string in dna]



def randomized_motif_searsh(dna, k, t):
    motifs = random_motif_genetator(dna, k)
    best_motifs = motifs
    while True:
        profile = profile_matrix(motifs)
        motifs = motifs_from_profile(dna, k, profile)
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs