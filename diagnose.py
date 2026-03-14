import pandas as pd

matched_players = pd.read_csv('Integration/matched_players_full.csv')
print('Seasons dtype:', matched_players['Seasons'].dtype)
print('Sample values:', matched_players['Seasons'].unique()[:10])

def get_season_start_end(season_str):
    if '/' in str(season_str):
        start, end = season_str.split('/')
        return pd.Timestamp(f'{int(start)}-07-01'), pd.Timestamp(f'{int(end)}-06-30')
    elif str(season_str).isdigit():
        year = int(season_str)
        return pd.Timestamp(f'{year}-01-01'), pd.Timestamp(f'{year}-12-31')
    else:
        return pd.NaT, pd.NaT

matched_players[['season_start', 'season_end']] = matched_players['Seasons'].apply(
    lambda x: pd.Series(get_season_start_end(x))
)
print('season_start dtype:', matched_players['season_start'].dtype)
print('Sample season_start:', matched_players['season_start'].head())
