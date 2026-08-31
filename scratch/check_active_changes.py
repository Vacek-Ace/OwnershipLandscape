import pandas as pd
import openpyxl

# Load active club seasons
active_df = pd.read_csv('data/active_club_season_ownership_and_transfers.csv')
print(f"Active clubs dataset rows: {len(active_df)}, unique clubs: {active_df['club_id'].nunique()}")

# Load Excel sheets
excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)
df_own = xl.parse('Ownership_Dataset')
df_sum = xl.parse('Ownership summary')
df_ev = xl.parse('Ownership events')

active_club_ids = set(active_df['club_id'].unique())
excel_club_ids = set(df_own['club_id'].unique())

print(f"Active club IDs in Excel: {len(active_club_ids.intersection(excel_club_ids))} / {len(active_club_ids)}")

# Let's see which active clubs had control changes
active_sum = df_sum[df_sum['Club ID'].isin(active_club_ids)]
active_changes = active_sum[active_sum['Cambio de control'] == 'Yes']
print(f"\nActive clubs in Big 5 that experienced a change of control: {len(active_changes)}")

# Let's inspect some of these active changes:
print("\nSample active clubs with control change:")
print(active_changes[['Club ID', 'Club', 'Liga', 'Propietario último al inicio del periodo', 'Propietario último al final del periodo', 'Fecha del cambio o cambios']].head(15).to_string())

