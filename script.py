import pandas as pd

input_path = r"D:\py\All _the _structures.csv"
output_path = r"D:\py\gap_transformed_output.xlsx"

df = pd.read_csv(input_path)

def generate_gap_rows(seq, struct, entry_id):
    rows = []
    n = len(seq)
    for gap in range(1, 5):
        group_count = gap + 1
        seq_groups = [""] * group_count
        struct_groups = [""] * group_count if pd.notnull(struct) else None

        for i in range(n):
            idx = i % group_count
            seq_groups[idx] += seq[i]
            if struct_groups is not None and i < len(struct):
                struct_groups[idx] += struct[i]

        for i in range(group_count):
            row = {
                "Entry": entry_id,
                "Original Sequence": seq,
                "Original Structure": struct if pd.notnull(struct) else None,
                "Gap": gap,
                "Group": i + 1,
                "Sequence Group": seq_groups[i],
                "Structure Group": struct_groups[i] if struct_groups else None
            }
            rows.append(row)
    return rows

all_rows = []
for idx, row in df.iterrows():
    sequence = row['sequence']
    structure = row.get('structure', None)
    all_rows.extend(generate_gap_rows(sequence, structure, idx + 1))

gap_df = pd.DataFrame(all_rows)
gap_df.to_excel(output_path, index=False)

print(f"✅ Output saved to: {output_path}")
