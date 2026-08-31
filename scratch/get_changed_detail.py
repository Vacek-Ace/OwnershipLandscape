import pandas as pd

excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)
df_own = xl.parse('Ownership_Dataset')
df_sum = xl.parse('Ownership summary')
df_ev = xl.parse('Ownership events')

active_df = pd.read_csv('data/active_club_season_ownership_and_transfers.csv')
active_ids = set(active_df['club_id'].unique())

active_sum = df_sum[df_sum['Club ID'].isin(active_ids)]
changed = active_sum[active_sum['Cambio de control'] == 'Yes']

print(f"Total active changed clubs: {len(changed)}")

rows = []
for _, r in changed.iterrows():
    cid = r['Club ID']
    cname = r['Club']
    league = r['Liga']
    start_owner = r['Propietario último al inicio del periodo']
    end_owner = r['Propietario último al final del periodo']
    dates = r['Fecha del cambio o cambios']
    op_type = r['Tipo de operación']
    final_model = df_own[df_own['club_id'] == cid]['ownership_model'].iloc[0]
    final_mco = df_own[df_own['club_id'] == cid]['mco'].iloc[0]
    final_state = df_own[df_own['club_id'] == cid]['state_link'].iloc[0]
    
    rows.append({
        'club_id': cid,
        'club_name': cname,
        'league': league,
        'start_owner': start_owner,
        'end_owner': end_owner,
        'dates': dates,
        'op_type': op_type,
        'final_model': final_model,
        'final_mco': final_mco,
        'final_state': final_state
    })

df_ch_detail = pd.DataFrame(rows)
df_ch_detail.to_csv('scratch/changed_active_clubs_detail.csv', index=False, encoding='utf-8')
print("Saved changed active clubs detail to scratch/changed_active_clubs_detail.csv")
