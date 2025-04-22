# Hydrophobicity scale map
hydrophobicity_scale = {
    'A': 1.80, 'C': 2.50, 'D': -3.50, 'E': -3.50,
    'F': 2.80, 'G': -0.40, 'H': -3.20, 'I': 4.50,
    'K': -3.90, 'L': 3.80, 'M': 1.90, 'N': -3.50,
    'P': -1.60, 'Q': -3.50, 'R': -4.50, 'S': -0.80,
    'T': -0.70, 'V': 4.20, 'W': -0.90, 'Y': -1.30
}

def gap_grouping(sequence, structure):
    n = len(sequence)
    result = []

    for gap in range(1, 5):
        group_data = []
        group_seqs = ['' for _ in range(gap + 1)]
        group_structs = ['' for _ in range(gap + 1)]

        for i in range(n):
            idx = i % (gap + 1)
            group_seqs[idx] += sequence[i]
            group_structs[idx] += structure[i]

        for i in range(gap + 1):
            group_seq = group_seqs[i]
            group_struct = group_structs[i]
            avg = round(sum(hydrophobicity_scale.get(c, 0) for c in group_seq) / len(group_seq), 2) if group_seq else 0.0

            group_data.append({
                "protein_sequence": group_seq,
                "average": avg,
                "structural_sequence": group_struct
            })

        result.append({
            "gap": gap,
            "sequences": group_data
        })

    return result

# Build final JSON data
final_json = []
for _, row in df.iterrows():
    sequence = row['sequence'].strip().upper()
    structure = row['structure'].strip().upper()
    if len(sequence) != len(structure):
        continue  # skip invalid entries
    final_json.append({
        "protein_sequence": sequence,
        "structural_sequence": structure,
        "sub_sequence": gap_grouping(sequence, structure)
    })

# Save to JSON file
output_path = "/mnt/data/sequence_structure_analysis.json"
with open(output_path, "w") as f:
    json.dump(final_json, f, indent=2)

output_path