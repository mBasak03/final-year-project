import json

hydrophobicity_scale = {
    'A': 1.80, 'C': 2.50, 'D': -3.50, 'E': -3.50, 'F': 2.80, 'G': -0.40,
    'H': -3.20, 'I': 4.50, 'K': -3.90, 'L': 3.80, 'M': 1.90, 'N': -3.50,
    'P': -1.60, 'Q': -3.50, 'R': -4.50, 'S': -0.80, 'T': -0.70, 'V': 4.20,
    'W': -0.90, 'Y': -1.30
}
def gap_print_with_structural(seq, struct_seq):
    n = len(seq)
    result = {
        "protein_sequence": seq,
        "structural_sequence": struct_seq,
        "sub_sequence": []
    }

    for gap in range(1, 5):
        sequences = []
        group_seqs = ['' for _ in range(gap + 1)]
        group_structs = ['' for _ in range(gap + 1)]

        for i in range(n):
            idx = i % (gap + 1)
            group_seqs[idx] += seq[i]
            group_structs[idx] += struct_seq[i]

        for i in range(gap + 1):
            protein_sequence = group_seqs[i]
            structural_sequence = group_structs[i]
            avg = (
                sum(hydrophobicity_scale.get(c, 0.0) for c in protein_sequence) /
                len(protein_sequence)
                if protein_sequence else 0.0
            )
            sequences.append({
                "protein_sequence": protein_sequence,
                "average": round(avg, 2),
                "structural_sequence": structural_sequence
            })

        result["sub_sequence"].append({
            "gap": gap,
            "sequences": sequences
        })

    print(json.dumps(result, indent=2))

# Input sequences
sequence = "MEPAAGIQRRSSQGPTVPPPPRGHAPPAAAPGPAPLSSPVREPPQLEEERQVRISESGQFSDGLEDRGLLESSTRLKPHEAQNYRKKALWVSWFSIIVTLALAVAAFTVSVMRYSASAFGFAFDAILDVLSSAIVLWRYSNAAAVHSAHREYIACVILGVIFLLSSICIVVKAIHDLSTRLLPEVDDFLFSVSILSGILCSILAVLKFMLGKVLTSRALITDGFNSLVGGVMGFSILLSAEVFKHDSAVWYLDGSIGVLIGLTIFAYGVKLLIDMVPRVRQTRHYEMFE"
structure = "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCHHHHHHHHHHHHHHHHHHHHHHHHHHHCCCCCHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHCCHHHHHHHHHHHHHHHHHHHHHHHHHCCCCCCCHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHCCCCCCCHHHHHHHHHHHHHHHHHHHHHHHHHHHHCCHHHHHHHHHHHHHHHHHHHHHHHHHHHHHCCCCCHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHCC"

gap_print_with_structural(sequence, structure)
