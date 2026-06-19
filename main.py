from dna_tools import *
from validators import is_valid

def main():
    user_seq = input("What DNA sequence do you want to analyze? ")

    DNA_seq = list(user_seq.upper())
    print("Sequence to study: " + "".join(DNA_seq))

    if is_valid(DNA_seq):
        nucleotide_count(DNA_seq)
        GC_percent = gc_percentage(DNA_seq)
        print(f"GC content: {GC_percent:.2f}%")

        comp_strand = get_complementary_strand(DNA_seq)
        print("Complementary strand: " + "".join(comp_strand))

        reverse_strand = reverse_complement(comp_strand)
        print("Reverse complement: " + "".join(reverse_strand))

        aa_strand = translate(DNA_seq)
        print("Amino acid sequence: " + " ".join(aa_strand))


if __name__ == "__main__":
    main()
