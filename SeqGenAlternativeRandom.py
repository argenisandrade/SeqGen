import random

def read_fasta_as_set(file_path):
    sequences = set()
    with open(file_path, 'r') as file:
        for line in file:
            # FASTA format: Odd lines are IDs (start with '>'), even lines are sequences
            if not line.startswith('>'):
                sequences.add(line.strip())  # Remove newline and add sequence to the set
    return sequences

def generate_unique_random_sequences(motifs, lengths=[4, 5, 6]):
    """
    Generates unique random sequences of specified lengths ensuring they are not in the given motif set.

    Args:
    motifs (set): A set of motifs to avoid.
    lengths (list): List of lengths for the random sequences to be generated.

    Returns:
    set: A set of unique random sequences.
    """
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'  # 20 standard amino acids
    unique_sequences = set()

    for length in lengths:
        while True:
            sequence = ''.join(random.choice(amino_acids) for _ in range(length))
            # Check if the sequence is unique and not in the motifs
            if sequence not in unique_sequences and sequence not in motifs:
                unique_sequences.add(sequence)
                break

    return unique_sequences

def set_to_length_mapped_dict(sequences_set):
    """
    Converts a set of sequences into a dictionary mapping the length of each sequence to the sequence itself.

    Args:
    sequences_set (set): A set of sequences.

    Returns:
    dict: A dictionary mapping the length of sequences to the sequences.
    """
    length_mapped_dict = {}
    for sequence in sequences_set:
        length_mapped_dict[len(sequence)] = sequence
    return length_mapped_dict

def replace_motifs_with_unique_sequences(sequence, motifs, unique_sequences):
    """
    Replaces motifs in the sequence with unique sequences of corresponding lengths.

    Args:
    sequence (str): The original amino acid sequence.
    motifs (set): A set of motifs to be replaced.
    unique_sequences (dict): A dictionary mapping lengths to unique sequences.

    Returns:
    str: Amino acid sequence with motifs replaced by unique sequences.
    """
    for motif in motifs:
        print('MOTIF BEING SCANNED: ' + str(motif))
        start = 0
        while True:
            start = sequence.find(motif, start)
            if start == -1:
                break
            end = start + len(motif)
            # Replace with a unique sequence of the same length
            replacement = unique_sequences.get(len(motif))
            if replacement:
                sequence = sequence[:start] + replacement + sequence[end:]
            start += len(motif)
    return sequence

def generate_random_amino_acid_sequence(min_length=10, max_length=50, motifs=None, unique_sequences=None):
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    length = random.randint(min_length, max_length)
    sequence = ''.join(random.choice(amino_acids) for _ in range(length))
    if motifs:
        sequence = replace_motifs_with_unique_sequences(sequence, motifs, unique_sequences)
    return sequence

# Example usage
fasta_file_path = 'motifs.fasta'  # Replace with the actual path to your FASTA file
motifs = read_fasta_as_set(fasta_file_path)
print('MOTIFS:')
print(motifs)
unique_random_sequences = generate_unique_random_sequences(motifs)
unique_sequences_dict = set_to_length_mapped_dict(unique_random_sequences)
print('DICTIONARY OF RANDOM SEQUENCES USED TO REPLACE:')
print(unique_sequences_dict)
random_sequence = generate_random_amino_acid_sequence(motifs=motifs, unique_sequences=unique_sequences_dict)
print('RANDOM SEQUENCE GENERATED:')
print(random_sequence)

