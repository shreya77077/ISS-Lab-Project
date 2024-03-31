def kasiski_examination(ciphertext, min_sequence_length=3):
    repeated_sequences = {}
    
    # Find repeated sequences of characters
    for i in range(len(ciphertext) - min_sequence_length + 1):
        sequence = ciphertext[i:i+min_sequence_length]
        if sequence in repeated_sequences:
            repeated_sequences[sequence].append(i)
        else:
            repeated_sequences[sequence] = [i]
    
    # Find distances between repeated sequences
    distances = {}
    for sequence, positions in repeated_sequences.items():
        if len(positions) > 1:
            distances[sequence] = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
    
    # Find common factors in distances
    common_factors = {}
    for sequence, seq_distances in distances.items():
        factors = []
        for i in range(len(seq_distances)):
            for j in range(i+1, len(seq_distances)):
                factors.extend(find_common_factors(seq_distances[i], seq_distances[j]))
        common_factors[sequence] = factors
    
    return common_factors

def find_common_factors(a, b):
    factors_a = get_factors(a)
    factors_b = get_factors(b)
    return list(set(factors_a) & set(factors_b))

def get_factors(n):
    factors = []
    for i in range(2, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

# Example usage
ciphertext = "ABCDABCDABCD"
common_factors = kasiski_examination(ciphertext)
print("Common factors in distances between repeated sequences:", common_factors)