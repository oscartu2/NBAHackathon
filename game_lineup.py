import pandas as pd

file = 'NBA Hackathon - Game Lineup Data Sample (50 Games).txt'

df = pd.read_csv(file, sep='\t', skiprows=(0))

print(df["Game_id"])