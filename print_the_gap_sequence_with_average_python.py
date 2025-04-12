hydrophobicity_scale = {
    'A': 1.80, 'C': 2.50, 'D': -3.50, 'E': -3.50,
    'F': 2.80, 'G': -0.40, 'H': -3.20, 'I': 4.50,
    'K': -3.90, 'L': 3.80, 'M': 1.90, 'N': -3.50,
    'P': -1.60, 'Q': -3.50, 'R': -4.50, 'S': -0.80,
    'T': -0.70, 'V': 4.20, 'W': -0.90, 'Y': -1.30
}

def group_by_gap_and_compute_hydrophobicity(seq):
    n = len(seq)
    gap = 1
    while gap <= 4:
        print(f"gap={gap}:")
        groups = ['' for _ in range(gap + 1)]

        for i in range(n):
            group_index = i % (gap + 1)
            groups[group_index] += seq[i]

        for group in groups:
            if group:
                total = sum(hydrophobicity_scale[c] for c in group)
                avg = total / len(group)
            else:
                avg = 0.0
            print(f"{group} average={avg:.2f}")
        gap += 1

# Example usage
group_by_gap_and_compute_hydrophobicity("SFTGTTGVQMGNDVYKIMLW")
