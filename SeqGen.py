import random

def read_fasta_as_set(file_path):
    """
    Reads a FASTA file and returns a set of sequences.

    Args:
    file_path (str): Path to the FASTA file.

    Returns:
    set: A set containing sequences from the FASTA file.
    """
    sequences = set()
    with open(file_path, 'r') as file:
        for line in file:
            # FASTA format: Odd lines are IDs (start with '>'), even lines are sequences
            if not line.startswith('>'):
                sequences.add(line.strip())  # Remove newline and add sequence to the set
    return sequences

def generate_random_amino_acid_sequence(min_length=10, max_length=50, excluded_motifs=None):
    if excluded_motifs is None:
        excluded_motifs = set()  # Add your motifs here, e.g., {'CYCR', 'RRRRH', 'RRWWC'}
    
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'  # 20 standard amino acids
    valid_sequence = False

    while not valid_sequence:
        length = random.randint(min_length, max_length)
        sequence = ''.join(random.choice(amino_acids) for _ in range(length))
        valid_sequence = all(motif not in sequence for motif in excluded_motifs)

    return sequence

# Example usage
fasta_file_path = 'motifs.fasta'  # Replace with the actual path to your FASTA file
motifs = read_fasta_as_set(fasta_file_path)
random_sequence = generate_random_amino_acid_sequence(excluded_motifs=motifs)
print(random_sequence)

