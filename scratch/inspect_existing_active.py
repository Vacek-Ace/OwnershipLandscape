import pandas as pd
import openpyxl

active_df = pd.read_csv('data/active_club_season_ownership_and_transfers.csv')
print("active_df shape:", active_df.shape)
print("active_df columns:", active_df.columns.tolist())
print(active_df.head(5).to_string())

excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)
print("Excel sheet names:", xl.sheet_names)

df_input = xl.parse('Input_Clubs')
print("Input_Clubs head(5):")
print(df_input.head(5).to_string())
