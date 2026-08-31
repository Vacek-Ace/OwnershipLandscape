import pandas as pd

excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)

print("=== METHOD NOTES ===")
df_notes = xl.parse('Method_Notes')
for idx, row in df_notes.iterrows():
    print(f"[{row['Field']}]: {row['Content']}")

print("\n=== SUMMARY ===")
df_summary = xl.parse('Summary')
for idx, row in df_summary.iterrows():
    print(f"[{row['Metric']}]: {row['Value']}")

print("\n=== OWNERSHIP SUMMARY BREAKDOWN ===")
df_own_sum = xl.parse('Ownership summary')
print("Cambio de control value counts:")
print(df_own_sum['Cambio de control'].value_counts(dropna=False))
print("\nNúmero de cambios de control value counts:")
print(df_own_sum['Número de cambios de control'].value_counts(dropna=False))
print("\nAdquisición minoritaria relevante value counts:")
print(df_own_sum['Adquisición minoritaria relevante'].value_counts(dropna=False))

print("\nClubs with 'Cambio de control' == 'Yes':")
changed_clubs = df_own_sum[df_own_sum['Cambio de control'] == 'Yes']
print(f"Total clubs with change of control: {len(changed_clubs)}")
print(changed_clubs[['Club ID', 'Club', 'Liga', 'Propietario último al inicio del periodo', 'Propietario último al final del periodo', 'Fecha del cambio o cambios', 'Tipo de operación']].to_string())

print("\n=== OWNERSHIP EVENTS BREAKDOWN ===")
df_events = xl.parse('Ownership events')
print("¿Produjo cambio de control? counts in events:")
print(df_events['¿Produjo cambio de control?'].value_counts(dropna=False))
print("\nEstado of events:")
print(df_events['Estado'].value_counts(dropna=False))
print("\nTop operation types in events:")
print(df_events['Tipo de operación'].value_counts().head(10))

