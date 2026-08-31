import pandas as pd
import openpyxl

# Load active club seasons
active_df = pd.read_csv('data/active_club_season_ownership_and_transfers.csv')
excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)
df_own = xl.parse('Ownership_Dataset')
df_sum = xl.parse('Ownership summary')
df_ev = xl.parse('Ownership events')

print(f"Total active club seasons: {len(active_df)}")
print(f"Seasons present: {sorted(active_df['season'].unique())}")
