import pandas as pd

df_clubs = pd.read_csv('data/dynamic_club_season_ownership.csv')
unknown_clubs = df_clubs[df_clubs['ownership_model'] == 'unknown']
print(f"Total club-seasons with ownership_model == 'unknown': {len(unknown_clubs)}")
print(unknown_clubs[['club_id', 'club_name', 'league', 'season', 'ultimate_owner', 'owner_type']])

df_ol = pd.read_csv('data/dynamic_ownership_landscape.csv')
print("\nMax prop_unknown in landscape across all 30 rows:")
print(df_ol[['league', 'season', 'prop_unknown']][df_ol['prop_unknown'] > 0])
