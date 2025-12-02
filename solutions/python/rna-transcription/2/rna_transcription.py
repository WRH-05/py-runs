def to_rna(dna_strand):
    RNA = ""
    complement = {"G":"C", "C":"G", "T":"A", "A":"U"}
    for _ in dna_strand:
        if _ == "G":
            RNA+= (complement["G"])
        elif _ == "C":
            RNA+= (complement["C"])
        elif _ == "T":
            RNA+= (complement["T"])
        else:
            RNA+= (complement["A"])
    return RNA