from data.genetic_code import codon_table
from data.complement import com_bases

def nucleotide_count(DNA_seq):
    print("Nucleotide count: " + str(len(DNA_seq)))

def gc_percentage(DNA_seq):
    return ((DNA_seq.count("G") + DNA_seq.count("C")) / len(DNA_seq)) * 100

def get_complementary_strand(DNA_seq):
    return [com_bases[n] for n in DNA_seq]


def reverse_complement(seq):
    return seq[::-1]

def translate(DNA_seq):
    codons = []
    for i in range(0, len(DNA_seq), 3):
        codon = "".join(DNA_seq[i:i+3])
        if len(codon) == 3:
            codons.append(codon)

    aa_seq = []
    for codon in codons:
        aa_seq.append(codon_table.get(codon, "X"))

    return aa_seq
