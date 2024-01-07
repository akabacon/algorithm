def align_sequences(seq1, seq2):
    gap_penalty = 2
    mismatch_penalty = 1

    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    # Initialize a matrix to store penalties
    penalties = [[0 for _ in range(len_seq2 + 1)] for _ in range(len_seq1 + 1)]

    # Fill the first row and column with gap penalties
    for i in range(len_seq1 + 1):
        penalties[i][0] = i * gap_penalty
    for j in range(len_seq2 + 1):
        penalties[0][j] = j * gap_penalty

    # Fill the matrix with penalties based on matches, mismatches, and gaps
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                match_penalty = 0
            else:
                match_penalty = mismatch_penalty
            penalties[i][j] = min(
                penalties[i - 1][j - 1] + match_penalty,
                penalties[i - 1][j] + gap_penalty,
                penalties[i][j - 1] + gap_penalty
            )

    # Traceback to find the aligned sequences
    aligned_seq1 = ""
    aligned_seq2 = ""
    i = len_seq1
    j = len_seq2
    while i > 0 or j > 0:
        if i > 0 and j > 0 and ((penalties[i][j] == penalties[i - 1][j - 1] and seq1[i - 1] == seq2[j - 1]) or penalties[i][j] == penalties[i - 1][j - 1] + mismatch_penalty):
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif i > 0 and penalties[i][j] == penalties[i - 1][j] + gap_penalty:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    # Calculate total penalty
    total_penalty = penalties[len_seq1][len_seq2]

    return total_penalty, aligned_seq1, aligned_seq2


def main():
    # Read input sequences
    seq1 = input().strip()
    seq2 = input().strip()

    # Align sequences
    penalty, aligned_seq1, aligned_seq2 = align_sequences(seq1, seq2)

    # Output results
    print(penalty)
    print(aligned_seq1)
    print(aligned_seq2)


if __name__ == "__main__":
    main()
