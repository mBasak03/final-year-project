import pandas as pd
import os
# // https://gist.github.com/mBasak03/998a36b5c90bb69bd8fb124db385de48

def gap_analysis(seq):
    if not isinstance(seq, str) or not seq:
        return {"Sequence": seq, "Error": "Invalid sequence"}
    
    n = len(seq)
    result = {"Sequence": seq}
    
    for gap in range(1, 5):
        groups = ["" for _ in range(gap + 1)]
        
        for i in range(n):
            groups[i % (gap + 1)] += seq[i]
        
        result[f"Gap {gap}"] = " | ".join(groups)
    
    return result

def process_excel(file_path):
    if not os.path.isfile(file_path) or not file_path.lower().endswith('.xlsx'):
        print("Invalid file path or format. Please provide a valid Excel (.xlsx) file.")
        return
    
    df = pd.read_excel(file_path, engine='openpyxl')
    if df.empty:
        print("The provided Excel file is empty.")
        return
    
    column_name = df.columns[0]
    sequences = df[column_name].dropna().astype(str).tolist()
    
    if not sequences:
        print("No valid sequences found in the file.")
        return
    
    results = [gap_analysis(seq) for seq in sequences]
    output_df = pd.DataFrame(results)
    output_file = os.path.join(os.path.dirname(file_path), "gap_analysis_results.xlsx")
    output_df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Results saved to: {output_file}")

file_path = input("Enter the full path of the Excel file: ")
process_excel(file_path)