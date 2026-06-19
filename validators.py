valid_bases = {"A", "T", "C", "G"}

def is_valid(DNA_seq):
    valid = True
    has_uracil = False
    U_index = []

    for index, base in enumerate(DNA_seq, start=1):
        if base == "U":
            U_index.append(index)
            has_uracil = True
            valid = False

        elif base not in valid_bases:
            print(f"Invalid base {base} at position {index}")
            valid = False

    if has_uracil:
        print(f"Uracil found at positions {U_index}")

    return valid
