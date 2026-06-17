# DNA Sequence Analysis Tool
Simple bioinformatics project for DNA sequence processing and translation

## Overview
This project was developed to combine my background in Biology with newly acquired programming skills in Python.
It provides a simple bioinformatics tool for analyzing DNA sequences and obtaining biologically relevant information.

## Features
- **Nucleotide count**: calculates the number of A, C, G, and T nucleotides in the sequence.
- **GC content**: computes the percentage of guanine (G) and cytosine (C), a key indicator of DNA stability.
- **Complementary strand**: generates the complementary DNA strand based on base-pairing rules (A-T, G-C).
- **Reverse complement**: produces the reverse complementary strand, a standard operation in molecular biology and bioinformatics.
- **Amino acid translation**: translates the DNA sequence into its corresponding amino acid sequence using the genetic code.

## Input validation
The program validates user input and detects invalid characters, reporting their position in the sequence.
- If uracil (U) is detected, the user is warned that the sequence may correspond to RNA instead of DNA.
- If an invalid nucleotide is detected (anything other than A, T, C or G), the program reports the error and its location.

## Programming concepts applied
This project helped reinforce several core Python concepts:

- Functions and modular programming
- String manipulation
- Dictionaries (base pairing rules and genetic code)
- Input validation and error handling
- Loops and conditional statements

## Future improvements

- Support for RNA sequences
- Reading frame selection
- FASTA file input support
- Expansion into a more complete bioinformatics toolkit
