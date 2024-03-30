def kasiski_examination(ciphertext):
    repeats = {}
    for i in range(len(ciphertext) - 3):  # Minimum length of repeated substring
        substr = ciphertext[i:i + 3]
        if substr in repeats:
            repeats[substr].append(i)
        else:
            repeats[substr] = [i]

    distances = {}
    for substr, positions in repeats.items():
        if len(positions) > 1:
            distances[substr] = [positions[j + 1] - positions[j] for j in range(len(positions) - 1)]

    factors = set()
    for sub_distances in distances.values():
        for i in range(len(sub_distances) - 1):
            for j in range(i + 1, len(sub_distances)):
                factors.add(sub_distances[j] - sub_distances[i])

    return factors

# Example usage:
ciphertext = "WFOHQZNSDWSFJJL"  # Intercepted ciphertext
keyword_lengths = kasiski_examination(ciphertext)
print("Possible keyword lengths:", keyword_lengths)
