import pandas as pd

# Load existing active panel
active_df = pd.read_csv('data/active_club_season_ownership_and_transfers.csv')

# Load Excel
excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)
df_own = xl.parse('Ownership_Dataset')
df_sum = xl.parse('Ownership summary')
df_ev = xl.parse('Ownership events')

print(f"Total active club-season rows: {len(active_df)}")
active_club_ids = set(active_df['club_id'].unique())

# Filter summary and events for active clubs
active_sum = df_sum[df_sum['Club ID'].isin(active_club_ids)]
active_changes = active_sum[active_sum['Cambio de control'] == 'Yes']

print(f"Active clubs with control changes: {len(active_changes)}")

# Let's inspect the events for these clubs
active_ev = df_ev[df_ev['Club ID'].isin(active_changes['Club ID'].unique())]
print(f"Events for active clubs with control change: {len(active_ev)}")

# Let's print out all these events to examine them carefully
for club_id in sorted(active_changes['Club ID'].unique()):
    c_name = active_changes[active_changes['Club ID'] == club_id]['Club'].iloc[0]
    c_league = active_changes[active_changes['Club ID'] == club_id]['Liga'].iloc[0]
    c_start_owner = active_changes[active_changes['Club ID'] == club_id]['Propietario último al inicio del periodo'].iloc[0]
    c_end_owner = active_changes[active_changes['Club ID'] == club_id]['Propietario último al final del periodo'].iloc[0]
    c_model_final = df_own[df_own['club_id'] == club_id]['ownership_model'].iloc[0]
    
    events = active_ev[active_ev['Club ID'] == club_id]
    print(f"\n--- Club {club_id}: {c_name} ({c_league}) ---")
    print(f"  Start owner (2019): {c_start_owner}")
    print(f"  End owner (2025): {c_end_owner}")
    print(f"  Final ownership model in dataset: {c_model_final}")
    for _, ev in events.iterrows():
        print(f"    Event: Date={ev['Fecha de cierre']}, Buyer={ev['Comprador']}, Seller={ev['Vendedor']}, ChangeControl={ev['¿Produjo cambio de control?']}, Status={ev['Estado']}, Type={ev['Tipo de operación']}")
