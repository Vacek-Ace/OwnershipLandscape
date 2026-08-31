import pandas as pd

excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)

output = []
output.append("=== SHEET OVERVIEW ===")
for sheet in xl.sheet_names:
    df = xl.parse(sheet, nrows=5)
    output.append(f"\n--- Sheet: {sheet} ---")
    output.append(f"Shape preview (first 5 rows): {df.shape}")
    output.append(f"Columns ({len(df.columns)}): {list(df.columns)}")

output.append("\n\n=== DETAILED ANALYSIS OF KEY SHEETS ===")

for sheet in xl.sheet_names:
    df = xl.parse(sheet)
    output.append(f"\n==========================================")
    output.append(f"SHEET: {sheet} (Total rows: {len(df)})")
    output.append(f"Columns: {list(df.columns)}")
    output.append("\nHead(3):")
    output.append(df.head(3).to_string())
    output.append("\nNull counts / Unique values:")
    for col in df.columns[:15]:
        output.append(f"  {col}: {df[col].nunique()} unique, {df[col].isnull().sum()} nulls")

with open('scratch/excel_inspection_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("Inspection completed and written to UTF-8")
