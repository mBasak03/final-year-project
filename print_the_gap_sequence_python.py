def gap_print(seq):
    n = len(seq)
    gap = 1
    while gap <= 4:
        print(f"gap={gap}:")
        groups = [""] * (gap + 1)  # Create groups for each `start`
        
        for i in range(n):
            group_index = i % (gap + 1)  # Determine the group based on modulo
            groups[group_index] += seq[i]
        
        for group in groups:  # Print each group's characters
            print(group)
        
        gap += 1

# Run the function with the given sequence
gap_print("SFTGTTGVQMGNDVYKIMLW")

# https://gist.github.com/mBasak03/998a36b5c90bb69bd8fb124db385de48
