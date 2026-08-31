import pandas as pd
import numpy as np

# 1. Load active club-seasons base
active_df = pd.read_csv('data/active_club_season_ownership_and_transfers.csv')

# Load Excel sheets
excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)
df_own = xl.parse('Ownership_Dataset')
df_sum = xl.parse('Ownership summary')
df_ev = xl.parse('Ownership events')

# Create a clean dictionary of base club info from Ownership_Dataset
base_info = {}
for _, r in df_own.iterrows():
    base_info[r['club_id']] = {
        'club_name': r['club_name'],
        'ultimate_owner': r['ultimate_owner'],
        'owner_country': r['owner_country'],
        'owner_origin': r['owner_origin'],
        'owner_type': r['owner_type'],
        'state_link': r['state_link'],
        'mco': r['mco'],
        'mco_group': r['mco_group'],
        'ownership_model': r['ownership_model']
    }

# Build full dynamic club-season panel
# We start with the consolidated base_info, then adjust historically for clubs with control changes
dynamic_rows = []

for _, row in active_df.iterrows():
    cid = row['club_id']
    cname = row['club_name']
    league = row['league']
    season = int(row['season'])
    squad_val = row['squad_market_value_eur']
    spending = row['transfer_spending_eur']
    income = row['transfer_income_eur']
    net_balance = row['net_transfer_balance_eur']
    
    # Start with base info
    info = base_info.get(cid, {}).copy()
    if not info:
        info = {
            'ultimate_owner': 'Unknown',
            'owner_country': 'Unknown',
            'owner_origin': 'unknown',
            'owner_type': 'unknown',
            'state_link': 0,
            'mco': 0,
            'mco_group': np.nan,
            'ownership_model': 'unknown'
        }
    
    # Now apply precise historical coding based on season:
    
    # 1. AC Milan (club_id = 5)
    # Changed 2022-08-31: Elliott -> RedBird (both investment fund, but MCO=0 under Elliott, MCO=1 under RedBird)
    if cid == 5:
        if season < 2022:
            info['ultimate_owner'] = 'Elliott Management'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 0
            info['mco_group'] = np.nan
        else:
            info['ultimate_owner'] = 'RedBird Capital Partners'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 1
            info['mco_group'] = 'RedBird football holdings'

    # 2. AS Roma (club_id = 12)
    # Changed 2020-08-17: Pallotta (foreign private) -> Friedkin Group (corporate-MCO)
    elif cid == 12:
        if season < 2020:
            info['ultimate_owner'] = 'James Pallotta'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'foreign private'
            info['mco'] = 0
            info['mco_group'] = np.nan
        else:
            info['ultimate_owner'] = 'The Friedkin Group'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'corporate-MCO'
            info['mco'] = 1
            info['mco_group'] = 'Friedkin Group'

    # 3. Everton (club_id = 29)
    # Farhad Moshiri through 2024 season (takeover closed Dec 2024, post-summer 2024)
    elif cid == 29:
        if season <= 2024:
            info['ultimate_owner'] = 'Farhad Moshiri'
            info['owner_country'] = 'United Kingdom / Iran'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'foreign private'
            info['mco'] = 0
            info['mco_group'] = np.nan

    # 4. Bordeaux (club_id = 40)
    # Changed 2021-07-23: King Street (investment fund) -> Gerard Lopez (foreign private / unknown)
    elif cid == 40:
        if season < 2021:
            info['ultimate_owner'] = 'King Street Capital Management'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'Gerard Lopez'
            info['owner_country'] = 'Spain / Luxembourg'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'unknown' # or foreign private
            info['mco'] = 0

    # 5. Inter Milan (club_id = 46)
    # Changed 2024-05-22: Suning/Zhang (foreign private) -> Oaktree (investment fund)
    elif cid == 46:
        if season < 2024:
            info['ultimate_owner'] = 'Suning Holdings Group / Zhang family'
            info['owner_country'] = 'China'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'foreign private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'Oaktree Capital Management'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 0

    # 6. Parma (club_id = 130)
    # Changed 2020-09-18: Nuovo Inizio (domestic private) -> Krause Group (foreign private) from 2021
    elif cid == 130:
        if season < 2021:
            info['ultimate_owner'] = 'Nuovo Inizio'
            info['owner_country'] = 'Italy'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'consortium / local business'
            info['ownership_model'] = 'domestic private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'Krause Group / Kyle Krause'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'foreign private'
            info['mco'] = 0

    # 7. Southampton (club_id = 180)
    # Changed 2022-01-04: Gao Jisheng (foreign private) -> Sport Republic (investment fund / MCO) from 2022
    elif cid == 180:
        if season < 2022:
            info['ultimate_owner'] = 'Gao Jisheng'
            info['owner_country'] = 'China'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'foreign private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'Sport Republic / Dragan Solak'
            info['owner_country'] = 'United Kingdom / Serbia'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 1

    # 8. Genoa (club_id = 252)
    # Changed 2021-09-23: Preziosi (domestic private) -> 777 Partners (investment fund / MCO) from 2022
    elif cid == 252:
        if season < 2022:
            info['ultimate_owner'] = 'Enrico Preziosi'
            info['owner_country'] = 'Italy'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = '777 Partners'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'foreign private' # or investment fund
            info['mco'] = 1

    # 9. Verona (club_id = 276)
    # Changed 2025-01-15: Setti (domestic private) throughout 2019-2024
    elif cid == 276:
        info['ultimate_owner'] = 'Maurizio Setti'
        info['owner_country'] = 'Italy'
        info['owner_origin'] = 'domestic'
        info['owner_type'] = 'private individual'
        info['ownership_model'] = 'domestic private'
        info['mco'] = 0

    # 10. Real Valladolid (club_id = 366)
    # Ronaldo Nazario throughout 2019-2024 (sale in 2025)
    elif cid == 366:
        info['ultimate_owner'] = 'Ronaldo Nazario'
        info['owner_country'] = 'Brazil'
        info['owner_origin'] = 'foreign'
        info['owner_type'] = 'private individual'
        info['ownership_model'] = 'foreign private'
        info['mco'] = 0

    # 11. Salernitana (club_id = 380)
    # Changed 2022-01-10: Lotito trust -> Iervolino (both domestic private)
    elif cid == 380:
        info['ownership_model'] = 'domestic private'
        info['mco'] = 0

    # 12. Leeds United (club_id = 399)
    # Changed 2023-07-17: Radrizzani (foreign private) -> 49ers Enterprises (foreign private)
    elif cid == 399:
        if season < 2023:
            info['ultimate_owner'] = 'Andrea Radrizzani / Aser Ventures'
            info['owner_country'] = 'Italy'
            info['ownership_model'] = 'foreign private'
        else:
            info['ultimate_owner'] = '49ers Enterprises'
            info['owner_country'] = 'United States'
            info['ownership_model'] = 'foreign private'

    # 13. Toulouse (club_id = 415)
    # Changed 2020-07-20: Sadran (domestic private) -> RedBird (investment fund / MCO) from 2020
    elif cid == 415:
        if season < 2020:
            info['ultimate_owner'] = 'Olivier Sadran'
            info['owner_country'] = 'France'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'RedBird Capital Partners'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 1

    # 14. Nice (club_id = 417)
    # Changed 2019-08-26: Chien Lee -> INEOS / Jim Ratcliffe (corporate-MCO from 2019)
    elif cid == 417:
        info['ultimate_owner'] = 'INEOS / Jim Ratcliffe'
        info['owner_country'] = 'United Kingdom'
        info['ownership_model'] = 'corporate-MCO'
        info['mco'] = 1

    # 15. Fiorentina (club_id = 430)
    # Changed 2019-06-06: Della Valle -> Commisso (foreign private from 2019)
    elif cid == 430:
        info['ultimate_owner'] = 'Rocco B. Commisso / Mediacom'
        info['owner_country'] = 'United States'
        info['ownership_model'] = 'foreign private'

    # 16. Hoffenheim (club_id = 533)
    # Changed 2023-11-29: Dietmar Hopp (domestic private) -> e.V. restoration (hybrid from 2024)
    elif cid == 533:
        if season < 2024:
            info['ultimate_owner'] = 'Dietmar Hopp'
            info['owner_country'] = 'Germany'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
        else:
            info['ultimate_owner'] = 'TSG 1899 Hoffenheim e.V. / Dietmar Hopp'
            info['owner_country'] = 'Germany'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'mixed'
            info['ownership_model'] = 'hybrid'

    # 17. Saint-Etienne (club_id = 618)
    # Changed 2024-06-03: Romeyer/Caiazzo (domestic private) -> Kilmer (foreign private from 2024)
    elif cid == 618:
        if season < 2024:
            info['ultimate_owner'] = 'Roland Romeyer and Bernard Caiazzo'
            info['owner_country'] = 'France'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
        else:
            info['ultimate_owner'] = 'Kilmer Sports Ventures / Larry Tanenbaum'
            info['owner_country'] = 'Canada'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'foreign private'

    # 18. Chelsea (club_id = 631)
    # Changed 2022-05-30: Abramovich (foreign private) -> BlueCo/Clearlake (investment fund / MCO from 2022)
    elif cid == 631:
        if season < 2022:
            info['ultimate_owner'] = 'Roman Abramovich'
            info['owner_country'] = 'Russia / Israel'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'foreign private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'BlueCo / Clearlake Capital-led consortium'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 1

    # 19. Strasbourg (club_id = 667)
    # Changed 2023-06-22: Marc Keller (domestic private) -> BlueCo (investment fund / MCO from 2023)
    elif cid == 667:
        if season < 2023:
            info['ultimate_owner'] = 'Marc Keller-led local shareholder group'
            info['owner_country'] = 'France'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'consortium / local business'
            info['ownership_model'] = 'domestic private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'BlueCo'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'
            info['mco'] = 1

    # 20. Ipswich Town (club_id = 677)
    # Changed 2021-04-07: Marcus Evans (domestic private) -> Gamechanger 20 / ORG (investment fund from 2021)
    elif cid == 677:
        if season < 2021:
            info['ultimate_owner'] = 'Marcus Evans'
            info['owner_country'] = 'United Kingdom'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
        else:
            info['ultimate_owner'] = 'Gamechanger 20 / ORG-led group'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'

    # 21. Espanyol (club_id = 714)
    # Rastar Group / Chen Yansheng through 2024 (takeover in Oct 2025)
    elif cid == 714:
        info['ultimate_owner'] = 'Rastar Group / Chen Yansheng'
        info['owner_country'] = 'China'
        info['owner_origin'] = 'foreign'
        info['owner_type'] = 'corporate group'
        info['ownership_model'] = 'foreign private'

    # 22. Le Havre (club_id = 738)
    # Vincent Volpe through 2024 (sale in 2025)
    elif cid == 738:
        info['ultimate_owner'] = 'Vincent Volpe'
        info['owner_country'] = 'United States'
        info['owner_origin'] = 'foreign'
        info['owner_type'] = 'private individual'
        info['ownership_model'] = 'foreign private'

    # 23. Newcastle (club_id = 762)
    # Changed 2021-10-07: Mike Ashley (domestic private) -> PIF (state-linked from 2022 / mid-2021)
    elif cid == 762:
        if season < 2022: # closed Oct 2021 post-summer window
            info['ultimate_owner'] = 'Mike Ashley'
            info['owner_country'] = 'United Kingdom'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
            info['state_link'] = 0
        else:
            info['ultimate_owner'] = 'PIF-led consortium'
            info['owner_country'] = 'Saudi Arabia'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'state-linked'
            info['ownership_model'] = 'state-linked'
            info['state_link'] = 2

    # 24. Atalanta (club_id = 800)
    # Changed 2022-02-19: Percassi (domestic private) -> Pagliuca/Percassi (hybrid / investment fund from 2022)
    elif cid == 800:
        if season < 2022:
            info['ultimate_owner'] = 'Percassi family'
            info['owner_country'] = 'Italy'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'family / private individual'
            info['ownership_model'] = 'domestic private'
        else:
            info['ultimate_owner'] = 'Stephen Pagliuca-led consortium with Percassi family'
            info['owner_country'] = 'United States / Italy'
            info['owner_origin'] = 'mixed'
            info['owner_type'] = 'mixed'
            info['ownership_model'] = 'hybrid'

    # 25. West Brom (club_id = 984)
    # Changed 2024-02-28: Guochuan Lai (foreign private) -> Patel family (foreign private)
    elif cid == 984:
        info['ownership_model'] = 'foreign private'

    # 26. Bournemouth (club_id = 989)
    # Changed 2022-12-13: Maxim Demin (foreign private) -> Black Knight / Bill Foley (corporate-MCO from 2023)
    elif cid == 989:
        if season < 2023:
            info['ultimate_owner'] = 'Maxim Demin'
            info['owner_country'] = 'United Kingdom / Russia'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'foreign private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'Black Knight Football Club / Bill Foley'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'corporate-MCO'
            info['mco'] = 1

    # 27. Sampdoria (club_id = 1038)
    # Changed 2023-05-31: Massimo Ferrero (domestic private) -> Gestio Capital (investment fund from 2023)
    elif cid == 1038:
        if season < 2023:
            info['ultimate_owner'] = 'Massimo Ferrero-related structure'
            info['owner_country'] = 'Italy'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
        else:
            info['ultimate_owner'] = 'Gestio Capital / Matteo Manfredi-led structure'
            info['owner_country'] = 'Italy / United Kingdom'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'

    # 28. Lyon (club_id = 1041)
    # Changed 2022-12-19: Aulas (domestic private/hybrid) -> Eagle Football / Textor (corporate-MCO from 2023)
    elif cid == 1041:
        if season < 2023:
            info['ultimate_owner'] = 'Jean-Michel Aulas / Holnest-led structure'
            info['owner_country'] = 'France'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'domestic private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'Eagle Football / John Textor'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'corporate-MCO'
            info['mco'] = 1

    # 29. Como (club_id = 1047)
    # Changed 2019-04-04: Hartono family (corporate-MCO from 2019)
    elif cid == 1047:
        info['ultimate_owner'] = 'SENT Entertainment / Hartono family'
        info['owner_country'] = 'Indonesia'
        info['owner_origin'] = 'foreign'
        info['owner_type'] = 'corporate group'
        info['ownership_model'] = 'corporate-MCO'
        info['mco'] = 1

    # 30. Lille (club_id = 1082)
    # Changed 2020-12-18: Gerard Lopez (foreign private) -> Merlyn Partners (investment fund from 2021)
    elif cid == 1082:
        if season < 2021:
            info['ultimate_owner'] = 'Gerard Lopez'
            info['owner_country'] = 'Spain / Luxembourg'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'foreign private'
        else:
            info['ultimate_owner'] = 'Merlyn Partners'
            info['owner_country'] = 'Luxembourg / United Kingdom'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'

    # 31. Troyes (club_id = 1095)
    # Changed 2020-09-02: Daniel Masoni (domestic private) -> City Football Group (state-linked / corporate-MCO from 2020)
    elif cid == 1095:
        if season < 2020:
            info['ultimate_owner'] = 'Daniel Masoni'
            info['owner_country'] = 'France'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
            info['mco'] = 0
            info['state_link'] = 0
        else:
            info['ultimate_owner'] = 'City Football Group'
            info['owner_country'] = 'United Arab Emirates'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'state-linked'
            info['ownership_model'] = 'state-linked'
            info['mco'] = 1
            info['state_link'] = 2

    # 32. Burnley (club_id = 1132)
    # Changed 2020-12-31: Mike Garlick (domestic private) -> ALK Capital (investment fund from 2021)
    elif cid == 1132:
        if season < 2021:
            info['ultimate_owner'] = 'Mike Garlick'
            info['owner_country'] = 'United Kingdom'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
        else:
            info['ultimate_owner'] = 'ALK Capital / Velocity Sports Partners'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'investment fund'
            info['ownership_model'] = 'investment fund'

    # 33. Leganes (club_id = 1244)
    # Changed 2022-06-23: Moreno Pavon (domestic private) -> Blue Crow Sports Group (corporate-MCO from 2022)
    elif cid == 1244:
        if season < 2022:
            info['ultimate_owner'] = 'Moreno Pavon family'
            info['owner_country'] = 'Spain'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'family / private individual'
            info['ownership_model'] = 'domestic private'
            info['mco'] = 0
        else:
            info['ultimate_owner'] = 'Blue Crow Sports Group'
            info['owner_country'] = 'United States'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'corporate group'
            info['ownership_model'] = 'corporate-MCO'
            info['mco'] = 1

    # 34. Elche (club_id = 1531)
    # Changed 2019-12-03: Sepulcre (domestic private) -> Bragarnik (foreign private from 2020)
    elif cid == 1531:
        if season < 2020:
            info['ultimate_owner'] = 'Jose Sepulcre-led structure'
            info['owner_country'] = 'Spain'
            info['owner_origin'] = 'domestic'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'domestic private'
        else:
            info['ultimate_owner'] = 'Christian Bragarnik'
            info['owner_country'] = 'Argentina'
            info['owner_origin'] = 'foreign'
            info['owner_type'] = 'private individual'
            info['ownership_model'] = 'foreign private'

    # 35. Almeria (club_id = 3302)
    # Changed 2019-08-02: Alfonso Garcia -> Turki Al-Sheikh / SMC Group (state-linked from 2019)
    elif cid == 3302:
        info['ultimate_owner'] = 'SMC Group / Mohamed Al-Khereiji / Turki Al-Sheikh'
        info['owner_country'] = 'Saudi Arabia'
        info['owner_origin'] = 'foreign'
        info['owner_type'] = 'state-linked'
        info['ownership_model'] = 'state-linked'
        info['state_link'] = 2
        info['mco'] = 0

    # 36. Monza (club_id = 2919)
    # Berlusconi / Fininvest throughout 2019-2024 (sale in late 2025)
    elif cid == 2919:
        info['ultimate_owner'] = 'Fininvest / Berlusconi family'
        info['owner_country'] = 'Italy'
        info['owner_origin'] = 'domestic'
        info['owner_type'] = 'corporate group'
        info['ownership_model'] = 'domestic private'
        info['mco'] = 0

    # Assemble row
    dynamic_rows.append({
        'club_id': cid,
        'club_name': cname,
        'league': league,
        'season': season,
        'squad_market_value_eur': squad_val,
        'transfer_spending_eur': spending,
        'transfer_income_eur': income,
        'net_transfer_balance_eur': net_balance,
        'ultimate_owner': info.get('ultimate_owner', 'Unknown'),
        'owner_country': info.get('owner_country', 'Unknown'),
        'owner_origin': info.get('owner_origin', 'unknown'),
        'owner_type': info.get('owner_type', 'unknown'),
        'ownership_model': info.get('ownership_model', 'unknown'),
        'mco': int(info.get('mco', 0)),
        'state_link': int(info.get('state_link', 0))
    })

df_dynamic_club = pd.DataFrame(dynamic_rows)
df_dynamic_club.to_csv('data/dynamic_club_season_ownership.csv', index=False, encoding='utf-8')
print("Successfully generated data/dynamic_club_season_ownership.csv (584 rows)")

# Now build the macro dynamic_ownership_landscape.csv (30 rows)
models = [
    'member-owned', 'domestic private', 'foreign private', 
    'investment fund', 'hybrid', 'corporate-MCO', 
    'state-linked', 'unknown'
]

landscape_rows = []
for (league, season), grp in df_dynamic_club.groupby(['league', 'season']):
    n_clubs = len(grp)
    counts = grp['ownership_model'].value_counts()
    props = {f'prop_{m}': counts.get(m, 0) / n_clubs for m in models}
    
    # Entropy
    p_vals = np.array([props[f'prop_{m}'] for m in models if props[f'prop_{m}'] > 0])
    entropy = - np.sum(p_vals * np.log(p_vals))
    
    # HHI
    hhi = np.sum([props[f'prop_{m}']**2 for m in models])
    
    # MCO rate
    mco_rate = (grp['mco'] == 1).sum() / n_clubs
    
    # State link rate
    state_link_rate = (grp['state_link'] > 0).sum() / n_clubs
    
    row_data = {
        'league': league,
        'season': season,
        'n_clubs': n_clubs,
        'entropy': entropy,
        'hhi': hhi,
        'mco_rate': mco_rate,
        'state_link_rate': state_link_rate
    }
    for m in models:
        row_data[f'prop_{m}'] = props[f'prop_{m}']
        row_data[f'count_{m}'] = counts.get(m, 0)
        
    landscape_rows.append(row_data)

df_dynamic_ol = pd.DataFrame(landscape_rows)
df_dynamic_ol.to_csv('data/dynamic_ownership_landscape.csv', index=False, encoding='utf-8')
print("Successfully generated data/dynamic_ownership_landscape.csv (30 rows)")

print("\n--- PREVIEW OF DYNAMIC OWNERSHIP LANDSCAPE ---")
print(df_dynamic_ol[['league', 'season', 'n_clubs', 'entropy', 'hhi', 'mco_rate', 'state_link_rate']].to_string())
