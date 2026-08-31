import pandas as pd
import openpyxl

excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)

df_own = xl.parse('Ownership_Dataset')
df_sum = xl.parse('Ownership summary')
df_ev = xl.parse('Ownership events')

print(f"Total clubs in Ownership_Dataset: {len(df_own)}")
print(f"Total clubs in Ownership summary: {len(df_sum)}")
print(f"Total events: {len(df_ev)}")

# Let's inspect clubs that changed control
changed = df_sum[df_sum['Cambio de control'] == 'Yes']
print(f"Clubs with Cambio de control == 'Yes': {len(changed)}")

# Let's inspect events that produced change of control
completed_control_events = df_ev[(df_ev['¿Produjo cambio de control?'] == 'Yes') & (df_ev['Estado'] == 'completed')]
print(f"Completed events with change of control: {len(completed_control_events)}")
print(completed_control_events[['Club ID', 'Club', 'Fecha de cierre', 'Propietario último anterior', 'Propietario último posterior', 'Tipo de operación']].head(10).to_string())
