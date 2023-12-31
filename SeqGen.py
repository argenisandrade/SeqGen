import random

def generate_random_amino_acid_sequence(min_length=10, max_length=50):
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'  # 20 standard amino acids
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(amino_acids) for _ in range(length))

# Example usage
random_sequence1 = generate_random_amino_acid_sequence()
print(random_sequence1)

random_sequence2 = generate_random_amino_acid_sequence()
print(random_sequence2)

random_sequence3 = generate_random_amino_acid_sequence()
print(random_sequence3)